from django.urls import path
from . import views


# URL config module
urlpatterns = [
    path('Products/', views.product_list), #shows all products
    path('Products/<int:id>/', views.product_detail), #shows product details by id
    path('Collections/', views.collection_list), #shows all collections
    path('Collections/<int:id>/', views.collection_detail) #shows collection details by id
]