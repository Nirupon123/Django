from django.urls import path
from . import views
from rest_framework_nested import routers

router=routers.DefaultRouter()
router.register('Products',views.ProductViewSet,basename='products')
router.register('Collections',views.collectionviewset,basename='collections')
router.register('Carts',views.CartViewSet,basename='carts')
router.register('customer',views.CustomerViewSet,basename='Customer')
router.register('orders',views.OrderViewSet,basename='orders')
router.register('images',views.ProductImageViewSet,basename='product-images')



product_router=routers.NestedDefaultRouter(router,'Products',lookup='product')
product_router.register('reviews',views.ReviewViewSet,basename='product-reviews')
product_router.register('images', views.ProductImageViewSet, basename='product-images')



cart_router=routers.NestedDefaultRouter(router,'Carts',lookup='cart')
cart_router.register('items',views.CartItemViewSet,basename='cart-items')



# URL config module
urlpatterns = router.urls + product_router.urls + cart_router.urls
