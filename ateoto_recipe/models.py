from django.db import models
from django.template.defaultfilters import slugify

class Ingredient(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(editable = False)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.q)
        
        super(Ingredient, self).save(*args, **kwargs)


class IngredientLine(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.CharField(max_length = 50)
    preparation = models.CharField(max_length = 50)
