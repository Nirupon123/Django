from django.urls import path
from . import views
from rest_framework_nested import routers

router=routers.DefaultRouter()
router.register('Products',views.ProductViewSet,basename='products')
router.register('Collections',views.collectionviewset,basename='collections')

product_router=routers.NestedDefaultRouter(router,'Products',lookup='product')
product_router.register('reviews',views.ReviewViewSet,basename='product-reviews')


# URL config module
urlpatterns = router.urls + product_router.urls 
