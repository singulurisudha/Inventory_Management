from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Supplier
from .serializers import SupplierSerializer

class SupplierAPIView(APIView):
    serializer_class = SupplierSerializer

    def get(self, request, pk=None):
        if pk:
            try:
                supplier = Supplier.objects.get(pk=pk)
                serializer = self.serializer_class(supplier)
                return Response(serializer.data)
            except Supplier.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)

        suppliers = Supplier.objects.all()
        serializer = self.serializer_class(suppliers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            supplier = Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(supplier, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            supplier = Supplier.objects.get(pk=pk)
        except Supplier.DoesNotExist:
            return Response({'msg':"Deleted Successfully....!!!"},status=status.HTTP_404_NOT_FOUND)

        supplier.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
