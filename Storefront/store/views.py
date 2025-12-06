from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product,Collection
from .serializer import ProductSerializer
from .serializer import CollectionSerializer
from rest_framework import status

# Collection list view
@api_view(['GET','POST'])
def collection_list(request):
    if request.method == 'GET':
        collection_set = Collection.objects.all()
        serializer = CollectionSerializer(collection_set, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CollectionSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# Collection detail view

@api_view(['GET','PUT','DELETE'])
def collection_detail(request,id):
        
        collection = get_object_or_404(Collection, pk=id)

        if request.method == 'GET':
            serializer = CollectionSerializer(collection)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CollectionSerializer(collection, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'DELETE':
            if collection.product_set.count() > 0:
                return Response(
                    {"error": "Collection cannot be deleted because it includes one or more products."},
                    status=status.HTTP_405_METHOD_NOT_ALLOWED,
                )
            collection.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def product_list(request):
    if request.method == 'GET':
        product_set = Product.objects.select_related('collection').all()
        serializer = ProductSerializer(product_set, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       
        

@api_view(['GET', 'PUT','DELETE'])
def product_detail(request,id):
        
        product = get_object_or_404(Product, pk=id)

        if request.method == 'GET':
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'DELETE':
            if product.orderitems.count() > 0:
                return Response(
                    {"error": "Product cannot be deleted because it is associated with an order item."},
                    status=status.HTTP_405_METHOD_NOT_ALLOWED,
                )
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
