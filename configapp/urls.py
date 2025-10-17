from django.urls import path
from .views import *


urlpatterns = [
    path("",index, name="home"),
    path("product/",product, name="product"),
    path('category/int:pk>/',category,name="category")
]