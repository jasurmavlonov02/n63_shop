from django.urls import path
from .views import index,product_detail,order_detail,create_product,delete_product,comment_create

app_name = 'shop'

urlpatterns = [
    # product crud
    path('',index,name='index'),
    path('category/<int:category_id>/',index, name='products_by_category'),
    path('detail/<int:product_id>/',product_detail,name='product_detail'),
    path('product/create/',create_product,name='create_product'),
    path('product/delete/<int:pk>/',delete_product,name='delete_product'),
    # order logic
  
    path('order/detail/<int:pk>/',order_detail,name='order_detail'),
    path('comment/create/<int:pk>',comment_create,name='comment_create')
]

