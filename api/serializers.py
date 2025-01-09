from rest_framework import serializers
from django.contrib.auth import get_user_model
from orders.models import Orders
from products.models import Products, Category
from rest_framework.authtoken.models import Token

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']
    

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'confirm_password']
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        confirm_password = validated_data.pop('confirm_password')
        email = validated_data.pop('email')
        
        if password == confirm_password:
            user = User.objects.create_user(email=email, password=password, **validated_data)
        else:
            raise ValueError('Password does not match')
        
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
    
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        model = Products
        fields = ['id', 'product_name', 'description', 'price', 'created_by', 'category']


class OrderSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    product = ProductSerializer(read_only=True)
    class Meta:
        model = Orders
        fields = ['id', 'product', 'created_by', 'status']