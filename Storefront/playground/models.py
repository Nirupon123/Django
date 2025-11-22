from django.db import models

class Products(models.Models):
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField()
    Inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)

class Customer(models.Models):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=255)
    birth_date=models.DateField(null=True)