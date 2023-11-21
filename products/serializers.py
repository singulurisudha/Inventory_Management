from rest_framework import serializers
from products.models import Product
from suppliers.models import Supplier


class ProductSerializer(serializers.ModelSerializer):
    supplier = serializers.CharField(max_length=100)
    class Meta:
        model = Product
        fields='__all__'
    
    def create(self, validated_data):
        supplier = validated_data.pop('supplier', None)
        if supplier:
            supplier, created = Supplier.objects.get_or_create(brand=supplier)
            validated_data['supplier'] = supplier
        return super().create(validated_data)
    def update(self, instance, validated_data):
        supplier_name = validated_data.pop('supplier', None)
        if supplier_name:
            supplier, created = Supplier.objects.get_or_create(brand=supplier_name)
            instance.supplier = supplier
        return super().update(instance, validated_data)