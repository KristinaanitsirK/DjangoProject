from django import forms
from django.core.exceptions import ValidationError
from .models import Product

class ProductForm(forms.ModelForm):
    description = forms.CharField(min_length=20)
    class Meta:
        model = Product
        # fields = '__all__'
        fields = ['name',
                  'description',
                  'quantity',
                  'category',
                  'price',
                  ]

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        description = cleaned_data.get('description')

        if name == description:
            raise ValidationError(
                'Description should not be identical to product name.'
            )

        return cleaned_data

    def clean_name(self):
        name = self.cleaned_data['name']
        if name[0].islower():
            raise ValidationError('Product name must begin with the capital letter.')
        return name



