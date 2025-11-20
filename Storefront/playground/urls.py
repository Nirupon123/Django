from django.urls import path
from . import views

# URL config module
urlpatterns = [
    path('hello/', views.say_hello)
]