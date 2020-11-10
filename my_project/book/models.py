from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext_lazy as _

# Create your models here.



class UserManager(BaseUserManager):
    def create_user(self,email,password,first_name,middile_name,last_name):
        user = self.model(
            email=email,
            password=password,
            first_name=first_name,
            middile_name=middile_name,
            last_name=last_name
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
        

    def create_superuser(self,email,password,first_name,middle_name,last_name):
        user = self.create_user(
            email=email,
            password=password,
            first_name=first_name,
            middile_name=middile_name,
            last_name=last_name           
        )
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(max_length=255)
    password = models.CharField(_('password'), max_length=128)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'middle_name']

    date_of_birth = models.DateField()
    GENDER_CHOICES = (
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('OTHER', 'Other'),
    )
    mobile_number = models.CharField(max_length=25)

    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES,
        blank=True
    )
    address = models.CharField(max_length=250)


    objects = UserManager()

    def __str__(self):
        return self.first_name()

class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name
   
class Product(models.Model):
    # user = models.ForeignKey(User,related_name='users',on_delete=models.CASCADE)
    category = models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
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