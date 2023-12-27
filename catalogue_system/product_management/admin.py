from django.contrib import admin
from .models import Product, AdminUser

# Register your models here.
admin.site.register(Product)
admin.site.register(AdminUser)
