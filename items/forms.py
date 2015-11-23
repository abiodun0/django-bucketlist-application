from django import forms
from django.forms import ModelForm, Textarea, TextInput, RadioSelect
from .models import Item


class ItemForm(ModelForm):
    

    class Meta:
        model = Item
        fields = ['name', 'description',]
        widgets = {
            'description': Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Items Description'}),
            'name': TextInput(attrs={
                'placeholder': 'Enter A name this item',
                'autocomplete': 'off',
                'class': 'form-control'
            }),
        }
