from django.shortcuts import render
from django.http import  HttpResponse
from django.db.models import Q,F
from store.models import Product

def say_hello(request):
    query_set = Product.objects.filter(Q(unit_price__gt=20) & Q(title__icontains='coffee'))
   # query_set = Product.objects.filter(unit_price__gt=F('collection__id') * 10)
    return render(request, 'index.html', {'products': list(query_set)})