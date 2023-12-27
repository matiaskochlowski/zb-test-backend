from django.db import models
from django.contrib.auth.models import AbstractUser

# Product model
class Product(models.Model):
    sku = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Custom Admin User model
class AdminUser(AbstractUser):
    # You can add additional fields if needed
    pass

    def __str__(self):
        return self.username
