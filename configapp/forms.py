from django import forms
from .models import Product, Suppliers, Category
import re
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            # 'photo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']

        if re.match(r'\d', title):
            raise ValidationError('Title raqam bolsin')

        return title


class SuppliersForm(forms.ModelForm):
    class Meta:
        model = Suppliers
        fields = '__all__'
        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_name': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_title': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'region': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_name(self):
        company_name = self.cleaned_data['company_name']

        if not re.match(r'^[A-Za-zА-Яа-я\s]+$', company_name):
            raise ValidationError(' company_name harf bolsin bolsin')

        return company_name


class CategoryForm(forms.ModelForm):
    class Meta():
        model = Category
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']

        if not re.match(r'^[A-Za-zА-Яа-я\s]+$', title):
            raise ValidationError(' title harf bolsin bolsin')

        return title




