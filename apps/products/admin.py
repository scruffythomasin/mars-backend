from django.contrib import admin
from .models import Product, Image, Attribute


admin.site.register((Product, Image, Attribute))