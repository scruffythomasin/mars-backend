from django.contrib import admin

from .models import User, UserProfile, UserProductRelation


admin.site.register((User, UserProfile, UserProductRelation))
