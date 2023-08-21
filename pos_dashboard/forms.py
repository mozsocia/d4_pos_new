from django import forms
from email.policy import default
from .models import *
from django.forms import inlineformset_factory
from django.utils import timezone
from django.forms import ModelChoiceField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

# Create your views here.
User = get_user_model()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields ='__all__'

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30,label='',
               widget=forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"User Name .."
               }) 
               )
    first_name = forms.CharField(max_length=30,label='',
               widget=forms.TextInput(attrs={
                   "class":"form-control",
                   "placeholder":"Enter your full name.."
               }) 
               )
    email = forms.EmailField(required=False,label='',
            widget=forms.TextInput(attrs={
                "class":"form-control",
                "placeholder":"Enter your email..(optional)"
            })
            )
    password1 = forms.CharField(max_length=30,label='',
               widget=forms.PasswordInput(attrs={
                   "class":"form-control",
                   "placeholder":"Password"
               }) 
               )
    password2 = forms.CharField(max_length=30,label='',
               widget=forms.PasswordInput(attrs={
                   "class":"form-control",
                   "placeholder":"confirmation Password"
               }) 
               )

    terms_and_conditions = forms.CharField(max_length=30,label='By signing up you agree to our terms and conditions.',
               widget=forms.CheckboxInput(attrs={
                   "class":"form-check-input tc_checkbox",          
               }) 
               )

    class Meta:
        model=User
        fields =['username', 'first_name', 'email','password1','password2']


class ProductForm(forms.ModelForm):
    aditional_discription = forms.CharField(required=False,widget=forms.Textarea(attrs={
        'class':'form-control p-20',
        'rows':"4"
    }))
    discription =forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control p-20',
        'rows':"4"
    }))
    flash_sale_add_and_expire_date = forms.DateTimeField(required=False, disabled=False,
                                          widget=forms.DateTimeInput(attrs={'type':'datetime-local'}))
    
    class Meta:
        model = Product
        fields = '__all__'


class SupplierAddForm(forms.ModelForm):
   
    
    class Meta:
        model = Supplier
        fields = ["name", "supplier_type", "supplier_ID", "address", "phone", "email", "start_date",
        "amount", "guarantor_name","guarantor_phone","Chassis_no","Transport_name","image"]


class Purchase_Product_Form(forms.ModelForm):
    class Meta:
        model = Purchase_Product
        fields = "__all__"


class Sales_Product_Form(forms.ModelForm):
    class Meta:
        model = Sales_Product
        fields = ["customer_name", "phone", "billing_date","sale_product_name","product_code",
        "category","brand","quantity","unit","unit_price",
        "sale_price","total_price","total_descount","sub_total","paid","due"]


class CategoryAddForm(forms.ModelForm):
    
    class Meta:
        model = Category
        fields =['category_name','parent','image']


class BrandAddForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields =['name','discription','image']


class UnitAddForm(forms.ModelForm):
    class Meta:
        model = Unit
        fields =['name']
        
class CustomersAddForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ["name", "customer_ID", "address", "phone", "email", "image"]        
        
        







