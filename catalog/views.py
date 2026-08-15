from django.utils.decorators import method_decorator
from rest_framework import viewsets
from catalog.permissions import IsOwnerOrReadOnly
from .models import Product
from catalog.serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from catalog.tasks import notify_new_product,invalidate_product_cache_list
from django.views.decorators.cache import cache_page

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['seller']
    @method_decorator(cache_page(60*2))
    def list(self,request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)

    def perform_create(self, serializer):
        instance = serializer.save(seller=self.request.user)
        notify_new_product.delay(instance.name)
        invalidate_product_cache_list.delay(instance.name)


