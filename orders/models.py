from django.db import models
from django.contrib.auth import get_user_model
from products.models import Products

User = get_user_model()

# Create your models here.
STATUES = (
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Delivered', 'Delivered'),
       
    )

class Orders(models.Model):
    product = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True, related_name="orders")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="orders")
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=STATUES, default='Pending')