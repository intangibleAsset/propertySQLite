from django import forms
from . models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
                'propertyReference',
                'seizedDate',
                'seizedTime',
                'description',
                'notes',
                #ForeignKeys
                'locationRecovered',
                'recoveredBy',
                'images',
                'owner',
                'operation',
        ]
