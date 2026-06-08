from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Recipe, Profile, Ingredient, RecipeIngredient
from .forms import RecipeForm, IngredientFormSet, ImageFormSet 


def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {"recipes": recipes}
    return render(request, "ledger/recipe_list.html", ctx)

def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    ctx = {"recipe": recipe}
    return render(request, "ledger/recipe_detail.html", ctx)


@login_required
def recipe_add(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        ingredient_formset= IngredientFormSet(request.POST, prefix='ingredients')
        image_formset = ImageFormSet(request.POST, request.FILES, prefix='images')

        if form.is_valid() and ingredient_formset.is_valid() and image_formset.is_valid():
            recipe = form.save(commit=False)
            profile, _ = Profile.objects.get_or_create(
                user=request.user,
                defaults={'name': request.user.username}
            )
            recipe.author = profile
            recipe.save()

            ingredient_formset.instance = recipe
            ingredient_formset.save()
            
            image_formset.instance = recipe
            images = image_formset.save(commit=False)
            for image in images:
                image.recipe = recipe
                image.save()

            return redirect('ledger:recipe-detail', pk=recipe.pk)
    else:
        form = RecipeForm()
        ingredient_formset = IngredientFormSet(prefix='ingredients')
        image_formset = ImageFormSet(prefix='images')

    ctx = {
        "form": form,
        "ingredient_formset": ingredient_formset,
        "image_formset": image_formset,
    }
    return render(request, "ledger/recipe_form.html", ctx)


@login_required
def recipe_edit(request,pk):
    recipe = get_object_or_404(Recipe, pk=pk)

    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        ingredient_formset = IngredientFormSet(request.POST, instance=recipe, prefix='ingredients')
        image_formset = ImageFormSet(request.POST, request.FILES, instance=recipe, prefix='images')
        
        if form.is_valid() and ingredient_formset.is_valid() and image_formset.is_valid():
            form.save()
            
            ingredient_formset.save()

            image_formset.instance = recipe            
            images = image_formset.save(commit=False)
            for image in images:
                image.recipe = recipe
                image.save()

            return redirect('ledger:recipe-detail', pk=recipe.pk)
    else:
        form = RecipeForm(instance=recipe)
        ingredient_formset = IngredientFormSet(instance=recipe, prefix='ingredients')
        image_formset = ImageFormSet(instance=recipe, prefix='images')
        
    ctx = {
    "form": form,
    "recipe": recipe,
    "ingredient_formset": ingredient_formset,
    "image_formset": image_formset,
    }
    return render(request, "ledger/recipe_form.html", ctx)
    

@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        recipe.delete()
        return redirect('ledger:recipe-list')
    ctx = {'recipe': recipe}
    return render(request, "ledger/recipe_delete.html", ctx)
