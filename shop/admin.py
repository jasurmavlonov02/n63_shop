from django.contrib import admin
from .models import Product, Category
from django.contrib.auth.models import User,Group
# Register your models here.

# admin.site.register(Product)
admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','discount','category']
    search_fields = ['name']
    list_filter = ['price']



admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.site_header = 'Najot Talim Admin'
admin.site.site_title = 'NT'
admin.site.index_title = "Welcome to UMSRA Researcher Portal"
