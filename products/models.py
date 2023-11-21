from django.db import models
from suppliers.models import Supplier

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    net_wt = models.CharField(max_length=120)
    created_at = models.DateTimeField(auto_now_add=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True,blank=True)

    def __str__(self):
        return self.name
