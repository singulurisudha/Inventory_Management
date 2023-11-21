from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from .serializers import (CustomUserRegistrationSerializer , CustomUserLoginSerializer ,
                CustomUserRoleSerializer,CustomUserModuleSerializer, CustomUserPermissionSerializer)
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .models import CustomUserRole , CustomUserPermission, CustomUserModule
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

# view for registering users
class CustomUserRegistrationView(APIView):
    def post(self, request):
        serializer = CustomUserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class CustomUserLoginView(TokenObtainPairView):
    serializer_class = CustomUserLoginSerializer

class CustomUserRoleView(APIView):
    def get(self, request, pk=None, *args, **kwargs):
        if pk:
            try:
                role = CustomUserRole.objects.get(pk=pk)
                serializer = CustomUserRoleSerializer(role)
                return Response(serializer.data)
            except CustomUserRole.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            roles = CustomUserRole.objects.all()
            serializer = CustomUserRoleSerializer(roles, many=True)
            return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CustomUserRoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, *args, **kwargs):
        try:
            role = CustomUserRole.objects.get(pk=pk)
            serializer = CustomUserRoleSerializer(role, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except CustomUserRole.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, *args, **kwargs):
        try:
            role = CustomUserRole.objects.get(pk=pk)
            role.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CustomUserRole.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
class CustomUserPermissionsView(APIView):
    def get(self, request, pk=None):
        if pk:
            permission = CustomUserPermission.objects.filter(pk=pk).first()
            if not permission:
                return Response({"error": "Permission not found"}, status=status.HTTP_404_NOT_FOUND)
            serializer = CustomUserPermissionSerializer(permission)
            return Response(serializer.data)
        else:
            permissions = CustomUserPermission.objects.all()
            serializer = CustomUserPermissionSerializer(permissions, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserPermissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        permission = CustomUserPermission.objects.filter(pk=pk).first()
        if not permission:
            return Response({"error": "Permission not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CustomUserPermissionSerializer(permission, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        permission = CustomUserPermission.objects.filter(pk=pk).first()
        if not permission:
            return Response({"error": "Permission not found"}, status=status.HTTP_404_NOT_FOUND)
        permission.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class CustomUserModuleView(APIView):
    def get(self, request, pk=None):
        if pk:
            module = get_object_or_404(CustomUserModule, pk=pk)
            serializer = CustomUserModuleSerializer(module)
            return Response(serializer.data)
        else:
            modules = CustomUserModule.objects.all()
            serializer = CustomUserModuleSerializer(modules, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        module = get_object_or_404(CustomUserModule, pk=pk)
        serializer = CustomUserModuleSerializer(module, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        module = get_object_or_404(CustomUserModule, pk=pk)
        module.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)