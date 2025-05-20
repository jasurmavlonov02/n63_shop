from django.contrib import admin
from .models import Product, Category,Order,Comment

from adminsortable2.admin import SortableAdminMixin

# Register your models here.

# admin.site.register(Product)
# admin.site.register(Category)
admin.site.register(Order)



class ProductInline(admin.StackedInline):
    model = Product
    extra = 2


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','title',]
    inlines = [
        ProductInline,
    ]

    
    

@admin.register(Product)
class ProductAdmin(SortableAdminMixin,admin.ModelAdmin):
    list_display = ['name','price','discount','category','created_at','my_order']
    search_fields = ['name']
    list_filter = ['price','category']



# admin.site.unregister(User)
# admin.site.unregister(Group)

admin.site.site_header = 'Najot Talim Admin'
admin.site.site_title = 'NT'
admin.site.index_title = "Welcome to UMSRA Researcher Portal"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name','email','rating','created_at','product']
    
    

