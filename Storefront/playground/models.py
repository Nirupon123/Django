from django.db import models

class Products(models.Models):
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField()
    Inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)

class Customer(models.Models):
    MEMBERSHIP_BRONZE='B'
    MEMBERSHIP_SILVER='S'
    MEMBERSHIP_GOLD='G'
    MEMBERSHIP_CHOICES=[
        (MEMBERSHIP_BRONZE,'Bronze'),
        (MEMBERSHIP_SILVER,'Silver'),
        (MEMBERSHIP_GOLD,'Gold'),
    ]
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField(unique=True)
    phone=models.CharField(max_length=255)
    birth_date=models.DateField(null=True)
    membership=models.CharField(max_length=1,MEMBERSHIP_CHOICES=MEMBERSHIP_CHOICES,default=MEMBERSHIP_BRONZE) 
class Order:
    PAYMENT_PENDING='P'
    PAYMENT_COMPLETE='C'
    PAYMENT_FAILED='F'
    PAYMENT_STATUS_CHOICES=[
        ( PAYMENT_PENDING,'Pending'),
        (PAYMENT_COMPLETE,'Complete'),
        (PAYMENT_FAILED,'Failed'),
    ]
    placed_at=models.DateTimeField(auto_now_add=True)
    payment_status=models.CharField(max_length=1,choices=PAYMENT_STATUS_CHOICES,default=PAYMENT_PENDING)

class Address(models.Models):
    street=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    customer=models.OneToOneField(Customer,on_delete=models.CASCADE)