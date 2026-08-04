from django.shortcuts import render
from rest_framework import viewsets

from catalog.models import Product
from catalog.serializers import ProductSerializer


# class ProductViewSet(viewsets.ReadOnlyModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

# Create your views here.
