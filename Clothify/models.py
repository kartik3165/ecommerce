from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products')
    brand = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.CharField(max_length=255)
    tags = models.CharField(max_length=100)
    desc = models.TextField()
    specification = models.TextField()

    def __str__(self):
        return self.name