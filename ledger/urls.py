from django.urls import path
from .views import recipe_detail, recipe_list, recipe_add, recipe_add_image, recipe_add_ingredient
urlpatterns = [
    path('recipes/list', recipe_list, name="recipe-list"),
    path('recipe/<int:pk>', recipe_detail, name="recipe-detail"),
    path('recipe/add', recipe_add, name="recipe-add"),
    path(
        'recipe/<int:pk>/add_image',
        recipe_add_image,
        name="recipe-add-image"
    ),
    path(
        'recipe/<int:pk>/add_ingredient',
        recipe_add_ingredient,
        name="recipe-add-ingredient"
    ),
]

app_name = "ledger"