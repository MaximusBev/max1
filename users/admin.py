from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Product

class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'role', 'is_staff', 'is_superuser')
    list_filter = ('role', 'is_staff', 'is_superuser')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Product)