from django.db import models
from decimal import Decimal
# Create your models here.


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    my_order = models.PositiveIntegerField(
        default=0,
        null=True,
        blank=True
    )
    
    class Meta:
        abstract = True
        

class Category(BaseModel):
    title = models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'categories'
        verbose_name = 'category'
        ordering = ['my_order']
        db_table = 'category'


class Product(BaseModel):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='products/')
    discount = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category,related_name='products',on_delete=models.SET_NULL,null=True,blank=True)
    amount = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.name

    
    @property
    def discounted_price(self):
        if self.discount > 0:
            return self.price * Decimal(f'{1 - (self.discount / 100)}')
        return self.price
    
    @property
    def get_absolute_url(self):
        if self.image:
            return self.image.url
        return ''
    
    class Meta:
        verbose_name_plural = 'products'
        verbose_name = 'product'
        ordering = ['my_order']
        db_table = 'product'



class Order(BaseModel):
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    quantity = models.PositiveIntegerField(default=1)
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='orders',
                                null=True,blank=True
                                )
    
    def __str__(self):
        return f'{self.name} - {self.quantity}'


    class Meta:
        db_table = 'order'


class Comment(BaseModel):
    class RatingChoices(models.IntegerChoices):
        ZERO = 0
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
        
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    product = models.ForeignKey(Product,on_delete=models.CASCADE,related_name='comments')
    rating = models.IntegerField(choices = RatingChoices.choices,default = RatingChoices.THREE.value)
    
    def __str__(self):
        return f'{self.name} - {self.rating}'
    
    class Meta:
        db_table = 'comment'