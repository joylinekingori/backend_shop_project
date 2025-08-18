from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=28)

class Tag(models.Model):
    name = models.CharField(max_length=28)

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)  
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)
    
    def __str__(self):
        return f'{self.name} || price {self.price}'
    
class Subscription(models.Model):
    name = models.CharField(max_length=50)

class Customer(models.Model):
    subscription = models.OneToOneField(Subscription, on_delete=models.CASCADE)

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True)

    def __str__(self):
        return self.name