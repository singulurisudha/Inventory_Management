from django.db import models
from products.models import Product
from suppliers.models import Supplier

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT)
    quantity_to_order = models.IntegerField()
    order_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateField()

    def __str__(self):
        return f"Order for {self.quantity_to_order} {self.product.name} from {self.supplier.brand}"
