from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Category(models.Model):
    CATEGORY_CHOICES = (
        ('Clothes', 'Clothes'),
        ('Tech', 'Tech'),
        ('Food', 'Food'),
        ('Kitchen', 'Kitchen'),
    )
    name = models.CharField(max_length=20, choices=CATEGORY_CHOICES)


class Products(models.Model):
    product_name = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    