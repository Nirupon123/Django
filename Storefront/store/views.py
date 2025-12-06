from .models import Product,Collection, Review
from django.shortcuts import get_object_or_404
from .serializer import ProductSerializer
from .serializer import CollectionSerializer
from .serializer import ReviewSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet



# Collection list view
class collectionviewset(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
    #def get_serializer_context(self):
            #return {'request': self.request}

    def destroy(self, request, id):
        collection = self.get_object(id)
        if collection.product_set.count() > 0:
            return Response(
                {"error": "Collection cannot be deleted because it includes one or more products."},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
        collection.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

         

# Product list view
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    #def get_serializer_context(self):
        #return {'request': self.request}

    def delete(self, request, id):
        product = self.get_object(id)
        if product.orderitems.count() > 0:
            return Response(
                {"error": "Product cannot be deleted because it is associated with an order item."},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
                )
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    #def get_serializer_context(self):
        #return {'request': self.request}
    def destroy(self, request, id):
        product = self.get_object(id)
        if product.orderitems.count() > 0:
            return Response(
                {"error": "Product cannot be deleted because it is associated with an order item."},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
                )
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



   
