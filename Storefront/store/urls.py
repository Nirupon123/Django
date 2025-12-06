from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router=SimpleRouter()
router.register('Products',views.ProductViewSet,basename='products')
router.register('Collections',views.collectionviewset,basename='collections')


# URL config module
urlpatterns = router.urls
