from django.contrib import admin

# Register your models here.
from .models import Product, ProductsCategory, ProductTag,ProductBrand
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('titel',)}
    list_display = ['titel', 'price', 'is_active']
    list_filter = ['titel', 'price', 'category', 'is_active']
    list_editable = ['price', 'is_active']

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductsCategory)
admin.site.register(ProductTag)
admin.site.register(ProductBrand)