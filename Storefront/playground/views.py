from django.shortcuts import render
from django.http import  HttpResponse
from django.db.models import Q,F
from store.models import Product,OrderItem
from store.models import Collection

def say_hello(request):
    #query_set = Product.objects.filter(Q(unit_price__gt=20) & Q(title__icontains='coffee'))
    #query_set = Product.objects.filter(unit_price__gt=F('collection__id') * 10)
    #query_set=OrderItem.objects.values('product_id').distinct()
    #tagedItems.objects.get_by_model(Product,1)
    collection = Collection()
    collection.title = "test_input"
    collection.featured_product = Product(pk=1)
    collection.save()

    return render(request, 'index.html')