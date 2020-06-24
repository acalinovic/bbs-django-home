from django.contrib import admin

from . BatchAdmin import BatchAdmin
from . BatchItemAdmin import BatchItemAdmin
from . GeneAdmin import GeneAdmin
from . IngredientAdmin import IngredientAdmin
from . NatureAdmin import NatureAdmin
from . ProgramAdmin import ProgramAdmin
from . RecipeAdmin import RecipeAdmin
from . RecipeItemAdmin import RecipeItemAdmin
admin.site.site_url = "/cookbook"
