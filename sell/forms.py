from django import forms
from .models import Vehicles

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicles
        fields = [
            'vehicle',
            'description',
            'produce_year',
            'price',
            'horsepower',
            'new_old',
            'image',
            'amount'
        ]

        widgets = {
                'vehicle': forms.TextInput(attrs={'class': 'form-control'}),
                'description': forms.Textarea(attrs={
                    'class': 'form-control',  # CSS class for styling
                    'rows': 5,  # Number of visible lines
                    'placeholder': 'Write your comment here...'
                }),
                'produce_year': forms.NumberInput(attrs={'class': 'form-control'}),
                'horsepower': forms.NumberInput(attrs={'class': 'form-control'}),
                'price': forms.NumberInput(attrs={'class': 'form-control'}),
                'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
                'new_old': forms.Select(attrs={'class': 'form-control'}),






            }