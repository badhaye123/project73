from django import forms
from .models import Product

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


        widgets={
             'Date':forms.SelectDateWidget()
         }
     