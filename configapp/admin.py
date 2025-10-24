from django.contrib import admin

from .models import *

admin.site.register([Category,Product,Suppliers,Order_details,Orders])