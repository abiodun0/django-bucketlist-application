from django import forms
from django.forms import ModelForm, Textarea, TextInput
from .models import BucketList


class BucketListForm(ModelForm):

    class Meta:
        model = BucketList
        fields = ['name', 'description']
        widgets = {
            'description': Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'BucketList Description'}),
            'name': TextInput(attrs={
                'placeholder': 'Enter A name for Your bucketlist',
                'autocomplete': 'off',
                'class': 'form-control'
            })
        }
