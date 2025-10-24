from django.urls import path
from .views import *


urlpatterns = [
    path("",index, name="home"),
    path('add_category/', add_category, name="add_category"),
    path('add_product/', add_product, name="add_product"),
    path('add_suppliers/',add_suppliers, name="add_suppliers"),
    path("product/",product, name="product"),
    path('category/<int:pk>/', category, name="category")

]
