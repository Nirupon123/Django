from .models import Product,Collection, Review, Cart, CartItem,Customer
from .serializer import ProductSerializer,CollectionSerializer,\
    ReviewSerializer,CartSerializer,CartItemSerializer,\
    CartItemSerializer,AddCartItemSerializer,UpdateCartItemSerializer,\
        DeleteCartItemSerializer,\
            CustomerSerializer
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,DjangoModelPermissions
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.viewsets import ModelViewSet,GenericViewSet
from rest_framework.pagination import PageNumberPagination
from rest_framework.mixins import ListModelMixin,CreateModelMixin, RetrieveModelMixin, DestroyModelMixin,UpdateModelMixin



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
    filter_backends = [DjangoFilterBackend]
    pagination_class = PageNumberPagination
    filterset_fields = ['collection_id']
    permission_classes = [IsAdminOrReadOnly]
    

    def get_serializer_context(self):
        return {'request': self.request}

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
    
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}
    



class CartViewSet(CreateModelMixin,RetrieveModelMixin,GenericViewSet,DestroyModelMixin):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    


class CartItemViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']


    def get_serializer_class(self):
        if self.request.method == 'POST':   
            return AddCartItemSerializer  
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        elif self.request.method == 'DELETE':
                return DeleteCartItemSerializer
        return CartItemSerializer 
    

    def get_serializer_context(self):
        return {'cart_id': self.kwargs['cart_pk']}

    def get_queryset(self):
        return CartItem.objects.\
            filter(cart_id=self.kwargs['cart_pk'])\
            .select_related('product')
    

class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [DjangoModelPermissions]         #permission group changing

    def get_permissions(self):
         if self.request.method =='GET':
             return [AllowAny()]
         return [IsAuthenticated()]


    @action(detail = False, methods = ['GET','PUT'])
    def me(self, request):
        
        (customer, created) = Customer.objects.get_or_create(user_id = request.user.id) # Get the customer for the logged-in user OR create one if it doesn't exist

        if request.method == 'GET':
            serializer = CustomerSerializer(customer) # Convert the customer model instance → JSON (serialization)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)  # Deserialize the incoming JSON → update the customer instance
            serializer.is_valid(raise_exception=True)  # CHECKING IF THE INPUT DATA IS VALID OR NOT
            serializer.save() #SAVING IT FOR THE UPDATED DATA  (JSON->QUERY) 
            return Response(serializer.data) #RETURN THE VALUE IN THE APPLICATION

        


  
   




   
