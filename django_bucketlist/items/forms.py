from django.forms import ModelForm, Textarea, TextInput, RadioSelect
from .models import Item


class ItemForm(ModelForm):

    """The model form for the Item Edit Form"""

    class Meta:
        DONE = [(True, 'Yes'), (False, 'No'), ]
        model = Item
        fields = ['name', 'description', 'done']
        widgets = {
            'description': Textarea(attrs={'class': 'form-control', 'rows': 2, 'placeholder': 'Items Description'}),
            'name': TextInput(attrs={
                'placeholder': 'Enter A name this item',
                'autocomplete': 'off',
                'class': 'form-control'
            }),
            'done': RadioSelect(choices=DONE, attrs={'class': 'radio-inline', }),
        }
