from django import forms
from shop.models import Order,Product,Comment

# class OrderForm(forms.Form): #forms.ModelForm
#     name = forms.CharField(max_length=150)
#     phone = forms.CharField(max_length=20)
#     quantity = forms.IntegerField(blank = True)


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # fields = ['name','phone','quantity']  
        exclude = ('created_at','updated_at','product')


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('created_at','updated_at','product')
        