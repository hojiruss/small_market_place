from rest_framework import viewsets
from catalog.permissions import IsOwnerOrReadOnly
from .models import Product
from catalog.serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from catalog.tasks import notify_new_product
from django.core.cache import cache
from rest_framework.response import Response

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['seller']

    def list(self,request,*args,**kwargs):
        cache_key = f'product_list:{request.get_full_path()}'
        cached_data = cache.get(cache_key)
        if cached_data is not None:
            return Response(cached_data)
        response = super().list(request,*args,**kwargs)
        cache.set(cache_key,response.data,timeout=60*5)
        return response

    def perform_create(self, serializer):
        instance = serializer.save(seller=self.request.user)
        notify_new_product.delay(instance.name)
        cache.delete_pattern('product_list:*')


    def perform_update(self,serializer):
        serializer.save()
        cache.delete_pattern('product_list:*')


    def perform_destroy(self,instance):
        instance.delete()
        cache.delete_pattern('product_list:*')


