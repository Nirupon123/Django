from django.db import models


class Collections(models.Models):
    title=models.CharField(max_length=255)

class Products(models.Models):
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.DecimalField()
    Inventory=models.IntegerField()
    last_update=models.DateTimeField(auto_now=True)
    collection=models.ForeignKey(Collections,on_delete=models.PROTECT)

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
class Order(models.Models):
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
    customer=models.ForeignKey(Customer,on_delete=models.PROTECT)


class OrderItem(models.Models):
    order=models.ForeignKey(Order,on_delete=models.PROTECT)
    product=models.ForeignKey(Products,on_delete=models.PROTECT)
    quantity=models.PositiveSmallIntegerField()
    unit_price=models.DecimalField(max_length=6,decimal_places=2)

class Address(models.Models):
    street=models.CharField(max_length=255)
    city=models.CharField(max_length=255)
    # Linking each Order to exactly one Customer.
    # OneToOneField ensures:
    #   - Each customer can have only one related order (1:1 relationship).
    #   - Each order belongs to exactly one customer.
    # on_delete=models.CASCADE means:
    #   - If a customer is deleted, the related order is automatically deleted.
    # primary_key=True makes this field the primary key for the Order model:
    #   - The Order will not have its own auto-generated 'id' field.
    #   - The customer's primary key becomes the order's primary key as well.
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)

class Cart(models.Models):
    created_at=models.DateTimeField(auto_now_add=True)
    
class CartItem(models.Models):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.PositiveSmallIntegerField()



