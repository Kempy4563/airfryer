from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'description', 'time', 'ingredients1', 'ingredients2', 'ingredients3', 'ingredients4', 'ingredients5', 'instructions1', 'instructions2', 'instructions3', 'instructions4', 'instructions5', 'image')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'border border-gray-300 rounded py-1 px-2 w-64'}),
            'description': forms.Textarea(attrs={'class': 'border border-gray-300 rounded py-1 px-2 w-64 h-32'}),
            'time': forms.TextInput(attrs={'class': 'border border-gray-300 rounded py-1 px-2 w-32'}),
            'ingredients1': forms.TextInput(attrs={'class': 'border border-gray-300 rounded py-1 px-2 w-64'}),
            'ingredients2': forms.TextInput(attrs={'class': 'border border-gray-300 rounded py-1 px-2 w-64'}),
            'ingredients3': forms.TextInput(attrs={'class': 'border border-gray-300 rounded py-1 px-2 w-64'}),
            'ingredients4': forms.TextInput(attrs={'class': 'border border-gray-300 rounded py-1 px-2 w-64'}),
            'ingredients5': forms.TextInput(attrs={'class': 'border border-gray-300 rounded py-1 px-2 w-64'}),
            'instructions1': forms.Textarea(attrs={'class': 'border border-gray-300 rounded py-1 px-2 w-64 h-32'}),
            'instructions2': forms.Textarea(attrs={'class': 'border border-gray-300 rounded py-1 px-2 w-64 h-32'}),
            'instructions3': forms.Textarea(attrs={'class': 'border border-gray-300 rounded py-1 px-2 w-64 h-32'}),
            'instructions4': forms.Textarea(attrs={'class': 'border border-gray-300 rounded py-1 px-2 w-64 h-32'}),
            'instructions5': forms.Textarea(attrs={'class': 'border border-gray-300 rounded py-1 px-2 w-64 h-32'}),
        }