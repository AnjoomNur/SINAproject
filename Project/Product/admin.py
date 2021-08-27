from django.contrib import admin

# Register your models here.
from Product.models import Category

admin.site.register(Category)