from rest_framework import serializers
from .models import CustomUser , CustomUserRole,CustomUserPermission, CustomUserModule
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomUserRegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length=120,write_only=True)
    class Meta:
        model = CustomUser
        fields = ['id','username','email','password','confirm_password','contact_number','address']

    def create(self, validated_data):
        user = CustomUser.objects.create(email=validated_data['email'],
                                       username=validated_data['username'],
                                       contact_number=validated_data['contact_number'],
                                       address=validated_data['address'],
                                         )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def validate(self, attrs):
        password = attrs.get('password')
        confirm_password = attrs.pop('confirm_password', None)
        if password != confirm_password:
            raise serializers.ValidationError("Passwords do not match")

        return attrs
  
class CustomUserLoginSerializer(TokenObtainPairSerializer):
    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
    
        if not username or not password:
            raise serializers.ValidationError("All fields are required")
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Wrong username or password")

        return super().validate(attrs)
    
class CustomUserRoleSerializer(serializers.ModelSerializer):
    users=serializers.SerializerMethodField()
    class Meta:
        model = CustomUserRole
        fields=['id','role','users']
    def get_users(self, value):
        return [user.username for user in value.users.all()]if value.users.exists() else []

class CustomUserModuleSerializer(serializers.ModelSerializer):
    created_by=serializers.CharField(max_length=120,read_only=True)
    class Meta:
        
        model = CustomUserModule
        fields = ['name', 'is_active', 'created_at', 'updated_at','created_by']
        read_only_fields = ['created_at', 'updated_at']

    def get_created_by(self, obj):
        if obj.created_by:
            return obj.created_by.username
        return None

    def validate_name(self, value):
        if not value:
            raise serializers.ValidationError("Name cannot be empty.")
        return value
    
class CustomUserPermissionSerializer(serializers.ModelSerializer):
    modules = serializers.SerializerMethodField()
    roles = serializers.SerializerMethodField()

    class Meta:
        model = CustomUserPermission
        fields = ['modules', 'roles']
    
    def get_modules(self, obj):
        return [module.name for module in obj.modules.all()]

    def get_roles(self, obj):
        return [role.role for role in obj.roles.all()]