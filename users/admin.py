from django.contrib import admin
from .models import Category, CustomUser

admin.site.register(Category)
admin.site.register(CustomUser)