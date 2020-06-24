from django.db import models
from cookbook.models import Recipe, Ingredient


class RecipeItem(models.Model):
    recipe = models.ForeignKey(Recipe, models.DO_NOTHING, blank=True, null=True)
    ingredient = models.ForeignKey(Ingredient, models.DO_NOTHING, blank=True, null=True)
    volume = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cookbook_recipe_item'

    def __str__(self):
        return self.ingredient.name
