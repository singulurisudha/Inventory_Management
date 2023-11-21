from django.urls import path
from .views import InventoryMovementView

urlpatterns = [
    path('inventory/', InventoryMovementView.as_view()),
    path('inventory/<int:pk>/', InventoryMovementView.as_view()),
]