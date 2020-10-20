import logging
from cookbook.models import Batch, BatchItem, Recipe, RecipeItem, Ingredient, Report, Gene


class BatchController:

    @staticmethod
    def batch_init(report: Report, gene: Gene):
        batch = Batch.objects.get_or_create(report=report, gene=gene)[0]
        batch.gene.used_in_batch = True
        batch.gene.save()
        for each in gene.recipe.recipe_items.all():
            BatchItem.manager.get_or_create(batch=batch, ingredient=each.ingredient)
        batch.save()

    @staticmethod
    def batch_compute(batch_id):
        logger = logging.getLogger(__name__)
        logger.warning('batch_compute start')
        batch = Batch.objects.get(id=batch_id)
        recipe = batch.gene.recipe
        recipe_items = dict()
        volumes_sum = 0.0
        for item in recipe.recipe_items.all():
            recipe_items[item.ingredient.name] = item
        for bi in batch.batch_items.exclude(ingredient_id=1):
            logger.warning(bi.ingredient.name)
            volume = recipe_items[bi.ingredient.name].volume * (batch.quantity + 4)
            bi.computed_vol = volume
            volumes_sum += volume
            bi.save()
        h2o = BatchItem.manager.get(ingredient_id=1, batch_id=batch_id)
        h2o_vol = (22 * (batch.quantity + 4)) - volumes_sum
        h2o.computed_vol = h2o_vol
        h2o.save()
        logger.warning('batch_compute stop')
        return batch
