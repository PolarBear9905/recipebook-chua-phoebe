from django import forms
from django.forms import inlineformset_factory
from .models import Recipe, RecipeImage, RecipeIngredient, Ingredient


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['name', 'description']


class RecipeIngredientForm(forms.ModelForm):
    ingredient = forms.ModelChoiceField(queryset=Ingredient.objects.all().order_by('name'))
    
    class Meta:
        model = RecipeIngredient
        fields = ['quantity', 'ingredient']

IngredientFormSet = inlineformset_factory(
    Recipe, RecipeIngredient,
    form=RecipeIngredientForm,
    extra=0,
    can_delete=True
)

ImageFormSet = inlineformset_factory(
    Recipe, RecipeImage,
    fields=['image'],
    extra=0, #sheesh django adds automatically blank slot so its gulo2 
    can_delete=True
)
