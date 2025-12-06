from rest_framework import serializers
from decimal import Decimal
from store.models import Product, Collection, Review



#product serializer defination
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title','inventory','description','slug', 'unit_price', 'price_with_tax', 'collection']
    price_with_tax = serializers.SerializerMethodField(method_name='get_price_with_tax')

    def get_price_with_tax(self, product) :
        return product.unit_price * Decimal(1.1)
    
#collection serializer defination
class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['id', 'title','featured_product'] 


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'name', 'description', 'date','product']