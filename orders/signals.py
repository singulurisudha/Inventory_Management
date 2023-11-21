from django.db.models.signals import post_save
from django.dispatch import receiver
from orders.models import Order
from inventory.models import InventoryMovement

@receiver(post_save, sender=Order)
def update_inventory(sender, instance, created, **kwargs):
    if created:  # If a new order is created
        ordered_quantity = instance.quantity_to_order
        
        # Fetch the inventory (assuming only one inventory instance exists)
        inventory = InventoryMovement.objects.first()
        
        if inventory:
            # Subtract ordered quantity from inventory
            inventory.quantity_of_stock -= ordered_quantity
            inventory.save()