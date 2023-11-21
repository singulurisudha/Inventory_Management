from django.contrib import admin
from inventory.models import InventoryMovement
from products.models import Product
from suppliers.models import Supplier
from orders.models import Order

admin.site.register(InventoryMovement)
admin.site.register(Product)
admin.site.register(Supplier)
admin.site.register(Order)
