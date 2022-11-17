from django.db import models

# Create your models here.
# from django.db import models

class Image(models.Model):
    # title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')

    

    title = models.CharField(
        max_length=100,
        
    )
    description = models.CharField(
        max_length=200,
       
    )
    date = models.DateField(
        
    )

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField("Email address", unique=True)
    age = models.IntegerField()
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Others', 'Others'),
    )
    gender=models.CharField(max_length=20 ,choices=GENDER)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    