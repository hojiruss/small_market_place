from rest_framework import serializers
from catalog.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name','price','stock_quantity','seller','description')
        read_only_fields = ('seller',)
