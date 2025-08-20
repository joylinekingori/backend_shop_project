from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=28)

class Tag(models.Model):
    name = models.CharField(max_length=28)

class Product(models.Model):
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)  
    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT)
    
    def __str__(self):
        return f'{self.name} || price {self.price}'
    
class Subscription(models.Model):
    name = models.CharField(max_length=50)

class Customer(models.Model):
    subscription = models.OneToOneField(Subscription, on_delete=models.CASCADE)
class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name}"


