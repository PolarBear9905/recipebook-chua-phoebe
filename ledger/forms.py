from django import forms
from .models import Recipe, RecipeImage, RecipeIngredient, Ingredient


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name']


class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        fields = ['image', 'description']


class RecipeIngredientForm(forms.ModelForm):
    ingredient = forms.ModelChoiceField(queryset=Ingredient.objects.all().order_by('name'))
    
    class Meta:
        model = RecipeIngredient
        fields = ['ingredient', 'quantity']