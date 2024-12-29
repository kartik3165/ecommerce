from django.db import models
from django.contrib.auth.models import User

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
    