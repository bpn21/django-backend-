from django.db import models
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
   
class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    user =models.ForeignKey(User,related_name='users',on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    size = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    brand = models.CharField(max_length= 30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    @property
    def category_name(self):
        return self.category.name