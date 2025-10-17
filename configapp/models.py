from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=100)


    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    photo = models.ImageField(upload_to='photo/%Y/%m/%d', blank=True, null=True)
    content = models.TextField(blank=True, null=True, verbose_name='Text')


    def __str__(self):
        return self.title






