from rest_framework import serializers
from .models import Order
from products.models import Product
from suppliers.models import Supplier
from products.serializers import ProductSerializer
from suppliers.serializers import SupplierSerializer

class OrderSerializer(serializers.ModelSerializer):
    product=serializers.CharField(max_length=100)
    supplier=serializers.CharField(max_length=100)
    class Meta:
        model = Order
        fields=('id', 'supplier', 'quantity_to_order', 'order_date', 'delivery_date', 'product')

    def get_supplier(self,obj):
        if obj.supplier:
            return obj.supplier.brand
    def get_products(self, obj):
        if obj.product:
            return obj.product.name
        
    def to_internal_value(self, data):
        product = data.get('product')
        try:
            product = Product.objects.get(name=product)
            
        except Product.DoesNotExist:
            pass
        
        return super().to_internal_value(data)

    def update(self, instance, validated_data):
        product_name = validated_data.pop('product', None)
        supplier_name = validated_data.pop('supplier', None)

        if product_name:
            product, created = Product.objects.get_or_create(name=product_name)
            instance.product = product

        if supplier_name:
            supplier, created = Supplier.objects.get_or_create(brand=supplier_name)
            instance.supplier = supplier

        return super().update(instance, validated_data)
    def create(self, validated_data):
        product = validated_data.pop('product')
        supplier = validated_data.pop('supplier')

        try:
            product = Product.objects.get(name=product)
            supplier = Supplier.objects.get(brand=supplier)

            order = Order.objects.create(
                product=product,
                supplier=supplier,
                quantity_to_order=validated_data['quantity_to_order'],
                order_date=validated_data.get('order_date'),
                delivery_date=validated_data.get('delivery_date')
            )
            return order
        except Product.DoesNotExist:
            raise serializers.ValidationError({"error": f"No product found with the name '{product}'"})
        except Supplier.DoesNotExist:
            raise serializers.ValidationError({"error": f"No supplier found with the name '{supplier}'"})

    