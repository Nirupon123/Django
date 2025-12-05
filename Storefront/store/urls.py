from django.urls import path
from . import views


# URL config module
urlpatterns = [
    path('Products/', views.product_list),
    path('Products/<int:id>/', views.product_detail)
]