from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)


    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    suppliers = models.ForeignKey('Suppliers', on_delete=models.CASCADE,default=1)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True, null=True)
    content = models.TextField(blank=True, null=True, verbose_name='Text')
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.title

class Suppliers(models.Model):
    company_name = models.CharField(max_length=100)
    contact_name = models.CharField(max_length=20)
    contact_title = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    country = models.CharField(max_length=100)


    def __str__(self):
        return self.company_name



class Order_details(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,default=1)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.CharField(max_length=1000)
    orders = models.ForeignKey('Orders',on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.product.title



class Orders(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    required_date = models.DateField()
    shipped_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return self.product.title




