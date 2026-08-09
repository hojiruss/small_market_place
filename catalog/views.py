from rest_framework import viewsets
from catalog.permissions import IsOwnerOrReadOnly
from .models import Product
from catalog.serializers import ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from catalog.tasks import notify_new_product

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['seller']

    def perform_create(self, serializer):
        serializer.save(seller=self.request.user)
        notify_new_product.delay(self.name)

