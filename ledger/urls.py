from django.urls import path
from .views import (recipe_detail, recipe_list, 
recipe_add, recipe_edit, recipe_delete)

urlpatterns = [
    path('recipes/list', recipe_list, name="recipe-list"),
    path('recipe/<int:pk>', recipe_detail, name="recipe-detail"),
    path('recipe/add', recipe_add, name="recipe-add"),
    path('recipe/<int:pk>/edit', recipe_edit, name="recipe-edit"),
    path('recipe/<int:pk>/delete', recipe_delete, name="recipe-delete"),
]

app_name = "ledger"