from django.db import models
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return self.name
   
class Product(models.Model):
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE, blank=True, null=True)
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