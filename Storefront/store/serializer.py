from rest_framework import serializers
from decimal import Decimal
from store.models import Product, Collection, Review, CartItem, Cart,Customer




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




class AddCartItemSerializer(serializers.ModelSerializer):

    product_id = serializers.IntegerField()
    
    def save(self, **kwargs):
        cart_id = self.context['cart_id']
        product_id = self.validated_data['product_id']
        quantity = self.validated_data['quantity']
        try:    
            cart_item = CartItem.objects.get(cart_id=cart_id, product_id=product_id)
            cart_item.quantity += quantity
            cart_item.save() 
            self.instance = cart_item
        except CartItem.DoesNotExist:
            self.instance=CartItem.objects.create(cart_id=cart_id,**self.validated_data)
        return self.instance
    
    class Meta:
        model = CartItem
        fields = ['id','product_id', 'quantity'] 



class UpdateCartItemSerializer(serializers.ModelSerializer):


    class Meta:
        model = CartItem
        fields = ['quantity']
    
    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance
      
class DeleteCartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['id']

    def delete(self, instance):
        instance.delete()
        return instance
    

class CustomerSerializer(serializers.ModelSerializer):

    user_id = serializers.IntegerField(read_only=True)
    class Meta:
        model=Customer
        fields=['id','user_id','phone','birth_date','membership']
   