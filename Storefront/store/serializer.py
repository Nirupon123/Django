from rest_framework import serializers
from decimal import Decimal
from store.models import Product, Collection, Review, CartItem, Cart



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
        fields = ['id', 'name', 'description', 'date']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Review.objects.create(product_id=product_id, **validated_data)
    

class CartItemSerializer(serializers.ModelSerializer):
    product=ProductSerializer()
    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity']



class CartSerializer(serializers.ModelSerializer):
    id=serializers.UUIDField(read_only=True)
    items=CartItemSerializer(many=True,read_only=True)
    totalprice = serializers.SerializerMethodField(method_name='get_total_price')

    def get_total_price(self, cart):
        return sum(item.product.unit_price * item.quantity for item in cart.items.all())
    class Meta:
        model = Cart
        fields = ['id','items','totalprice']



