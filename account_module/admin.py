from django.contrib import admin
from .models import User


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    name = 'User'
    verbose_name = 'کاربر'
    verbose_name_plural = verbose_name+'ان'
    list_display = ['username', 'email', 'is_staff', 'is_active']
    list_filter = ['is_staff', 'is_active']
    search_fields = ['username', 'email']

admin.site.register(User, UserAdmin)
