from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Products(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products')
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    # CATEGORY_LIST = [('T-shirt', 'T-shirt'), ('Hoodies', 'Hoodies'),('Shirt,', 'Shirt'),('Jacket', 'Jacket')]
    # category = models.CharField(max_length=255, choices=CATEGORY_LIST, default='T-shirt')
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    tags = models.CharField(max_length=100)
    desc = models.TextField()
    specification = models.TextField()

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    user = models.ForeignKey(User, related_name='customer', on_delete=models.CASCADE)
    product = models.ManyToManyField(to=Products, related_name='cart_products', blank=True)

    def __str__(self):
        return self.user.first_name
    

class Order(models.Model):
    order_id = models.CharField(max_length=50) # to identify order group
    user = models.ForeignKey(User, related_name='order_customer', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, related_name='order_item', on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    mobile_no = models.CharField(max_length=10)
    date = models.DateTimeField(default=datetime.now())
    STATUS_CHOICES = [('Pending', 'Pending'), ('Delivered', 'Delivered'), ('On the Way', 'On the way')]
    status = models.CharField(max_length=50, choices= STATUS_CHOICES, default='pending')

    def __str__(self):
        return f'{self.product.name} - {self.user.first_name}'