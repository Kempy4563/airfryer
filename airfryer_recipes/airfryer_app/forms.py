from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = (
            'name',
            'description',
            'time',
            'ingredients1',
            'ingredients2',
            'ingredients3',
            'ingredients4',
            'ingredients5',
            'instructions1',
            'instructions2',
            'instructions3',
            'instructions4',
            'instructions5',
            'image',
        )
        widgets = {
            'name': forms.TextInput(attrs={'class': 'wide-input'}),
            'description': forms.Textarea(attrs={'class': 'wide-input'}),
            'time': forms.TextInput(attrs={'class': 'wide-input'}),
            'ingredients1': forms.TextInput(attrs={'class': 'wide-input'}),
            'ingredients2': forms.TextInput(attrs={'class': 'wide-input'}),
            'ingredients3': forms.TextInput(attrs={'class': 'wide-input'}),
            'ingredients4': forms.TextInput(attrs={'class': 'wide-input'}),
            'ingredients5': forms.TextInput(attrs={'class': 'wide-input'}),
            'instructions1': forms.Textarea(attrs={'class': 'wide-input'}),
            'instructions2': forms.Textarea(attrs={'class': 'wide-input'}),
            'instructions3': forms.Textarea(attrs={'class': 'wide-input'}),
            'instructions4': forms.Textarea(attrs={'class': 'wide-input'}),
            'instructions5': forms.Textarea(attrs={'class': 'wide-input'}),
            'image': forms.FileInput(attrs={'class': 'wide-input'}),
        }