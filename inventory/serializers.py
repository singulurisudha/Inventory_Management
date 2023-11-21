from rest_framework import serializers
from inventory.models import InventoryMovement
from products.models import Product
from suppliers.models import Supplier
from orders.models import Order

class InventoryMovementSerializer(serializers.ModelSerializer):
    product=serializers.CharField(max_length=120)
    supplier=serializers.CharField(max_length=120)
    class Meta:
        model = InventoryMovement
        fields = ('id', 'product','supplier', 'quantity_of_stock', 'movement_type', 'movement_date')

    def create(self, validated_data):
        product = validated_data.pop('product')
        supplier = validated_data.pop('supplier')

        try:
            product = Product.objects.get(name=product)
            supplier = Supplier.objects.get(brand=supplier)

            inventory = InventoryMovement.objects.create(
                product=product,
                supplier=supplier,
                quantity_of_stock=validated_data['quantity_of_stock'],
                movement_type=validated_data.get('movement_type'),
                movement_date=validated_data.get('movement_date')
            )
            return inventory
        except Product.DoesNotExist:
            raise serializers.ValidationError({"error": f"No product found with the name '{product}'"})
        except Supplier.DoesNotExist:
            raise serializers.ValidationError({"error": f"No supplier found with the name '{supplier}'"})
    def get_supplier(self, obj):
        if obj.supplier :
            return obj.supplier.brand

    def update(self, instance, validated_data):
        product_name = validated_data.get('product')
        supplier_name= validated_data.get('supplier')
        if product_name:
            try:
                product = Product.objects.get(name=product_name)
                instance.product = product
            except Product.DoesNotExist:
                raise serializers.ValidationError({"error": f"No product found with the name '{product_name}'"})
        if supplier_name:
            try:
                supplier = Supplier.objects.get(brand=supplier_name)
                instance.supplier = supplier
            except Supplier.DoesNotExist:
                raise serializers.ValidationError({"error": f"No supplier found with the name '{supplier_name}'"})
        instance.quantity_of_stock = validated_data.get('quantity_of_stock', instance.quantity_of_stock)
        instance.movement_type = validated_data.get('movement_type', instance.movement_type)
        instance.movement_date = validated_data.get('movement_date', instance.movement_date)
        instance.save()
        return instance