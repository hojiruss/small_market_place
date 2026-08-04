from rest_framework import serializers
from catalog.models import Product

class ProductSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = serializers.DecimalField(max_digits=10, decimal_places=2)
    seller = serializers.IntegerField()
    description = serializers.CharField(max_length=200)
    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.price)
        instance.stock_quantity = validated_data.get('stock_quantity', instance.stock_quantity)
        instance.seller = validated_data.get('seller', instance.seller)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance

    def delete(self,instance):
        instance.delete()
        return True