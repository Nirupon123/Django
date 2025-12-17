from django.shortcuts import render
from django.http import  HttpResponse
from django.db.models import Q,F
from store.models import Product,OrderItem
from store.models import Collection,Order
from django.db import transaction
from django.core.mail import send_mail,BadHeaderError,mail_admins

def say_hello(request):
    #query_set = Product.objects.filter(Q(unit_price__gt=20) & Q(title__icontains='coffee'))
    #query_set = Product.objects.filter(unit_price__gt=F('collection__id') * 10)
    #query_set=OrderItem.objects.values('product_id').distinct()
    #tagedItems.objects.get_by_model(Product,1)

    #updating DB nwith new objects

    #collection = Collection(pk=11)
    #collection.delete()
    #collection.title = "test_input"
    #collection.featured_product = Product(pk=1)
    #collection.save()

    #updating objects from DB

    #Collection.objects.filter(pk=11).update(title="NEW PRODUCT")

    #deleing objects from DB

    #Collection.objects.filter(id__gt=10).delete()
    
    #transactions(ACID-Atomicity)
#     with transaction.atomic():
#             order = Order()
#             order.customer_id=1
#             order.save()

#             item=OrderItem()
#             item.order=order
#             item.product_id=1
#             item.quantity=1
#             item.unit_price=10
#             item.save()

        try:   
                send_mail(subject='mailcheck',message='this is a test mail',from_email='toilaktonigga@example.com',recipient_list=['uddalaknigga@example.com'])
        except BadHeaderError:
                pass
        return render(request,'index.html',{'name':'Nirupon'})