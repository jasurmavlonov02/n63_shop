from django.contrib import admin
from .models import Product, Category,Order,Comment
from django.contrib.auth.models import User,Group
# Register your models here.

# admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','discount','category','created_at']
    search_fields = ['name']
    list_filter = ['price']



admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.site_header = 'Najot Talim Admin'
admin.site.site_title = 'NT'
admin.site.index_title = "Welcome to UMSRA Researcher Portal"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','rating','created_at','product']
    