from django.urls import path
from .views import SupplierAPIView

urlpatterns = [
    path('suppliers/', SupplierAPIView.as_view(), name='supplier-list-create'),
    path('suppliers/<int:pk>/', SupplierAPIView.as_view(), name='supplier-detail'),
]