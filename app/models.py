from distutils.command.upload import upload
from django.core.validators import MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATE_CHOICES = (
    ('Maharshtra' ,'Maharashtra'),
    ('Gujrat' , 'Gujrat'),('Up','Up'),
    ('Rajasthan','Rajasthan'),
    ('Delhi','Delhi')
)

class Customer(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    locality = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES , max_length=50)

    def __str__(self):
        return str(self.name)
    

CATEGORY_CHOICES = (
    ('M' , 'Mobile'),
    ('L', 'Laptop'),
    ('HA', 'Home Applaince'),
    ('G' , 'Grocceory'),
    ('BW','Bottom Wear'),
    ('TW', 'Top Wear'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    brand = models.CharField(max_length=50)
    category = models.CharField(choices=CATEGORY_CHOICES , max_length=3)
    product_img = models.ImageField(upload_to='producting')

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)


ORDER_CHOICE = (
    ('ACCEPTED', 'ACCECPTED'),
    ('PACKED' , 'PACKED'),
    ('ON THE WAY','ON THE WAY'),
    ('DELIVERED' , 'DELIVERED'),
    ('CANCEL' , 'CANCEL'),
)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now=True)
    status =  models.CharField(max_length=20,choices=ORDER_CHOICE , default="Pending")

    def __str__(self):
        return str(self.id)



