from django.db import models

class Products(models.Models):
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField()