from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from recipebook.storage import CloudinaryStorage


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    short_bio = models.TextField()

    def __str__(self):
        return '{}'.format(self.name)


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return reverse('ledger:ingredient-detail', args=[str(self.pk)])


class Recipe(models.Model):
    name = models.CharField(max_length=100)

    author = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='recipes',
        null=True,
        blank=True
    )

    description = models.TextField()

    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.name)

    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[str(self.pk)])
    
    class Meta:
        ordering = ['name']
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)

    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipe'
    )

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='ingredients'
    )


class RecipeImage(models.Model):
    image = models.ImageField(
        upload_to='images/',
        storage=CloudinaryStorage(),
        max_length=500,
        null=False
    )

    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='images'
    )