from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe, Profile
from .forms import RecipeForm, RecipeImageForm, RecipeIngredientForm


def recipe_list(request):
    recipes = Recipe.objects.all()
    ctx = {"recipes": recipes}
    return render(request, "ledger/recipe_list.html", ctx)


@login_required
def recipe_detail(request, pk):
    ctx = {"recipe": Recipe.objects.get(pk=pk)}
    return render(request, "ledger/recipe_detail.html", ctx)


@login_required
def recipe_add(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            profile, _ = Profile.objects.get_or_create(
                user=request.user,
                defaults={'name': request.user.username}
            )
            recipe.author = profile
            recipe.save()
            return redirect('ledger:recipe-detail', pk=recipe.pk)
    else:
        form = RecipeForm()

    ctx = {"form": form}
    return render(request, "ledger/recipe_form.html", ctx)


@login_required
def recipe_add_image(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == "POST":
        form = RecipeImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.recipe = recipe
            image.save()
            return redirect('ledger:recipe-detail', pk=recipe.pk)
    else:
        form = RecipeImageForm()

    ctx = {"form": form, "recipe": recipe}
    return render(request, "ledger/recipe_form_generic.html", ctx)

@login_required
def recipe_add_ingredient(request, pk):
    recipe = Recipe.objects.get(pk=pk)

    if request.method == "POST":
        form = RecipeIngredientForm(request.POST)
        if form.is_valid():
            ingredient = form.save(commit=False)
            ingredient.recipe = recipe
            ingredient.save()
            return redirect('ledger:recipe-detail', pk=recipe.pk)
    else:
        form = RecipeIngredientForm()
    
    ctx = {"form": form, "recipe": recipe}
    return render(request, "ledger/recipe_form_generic.html", ctx)

