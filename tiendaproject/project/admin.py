from django.contrib import admin
from .models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'stock', 'category', 'image')
    search_fields = ('name', 'description')
    list_filter = ('category',)
    fields = ('name', 'description', 'price', 'stock', 'category', 'image')

admin.site.register(Category, CategoryAdmin)
try:
    admin.site.register(Product, ProductAdmin)
except admin.sites.AlreadyRegistered:
    pass