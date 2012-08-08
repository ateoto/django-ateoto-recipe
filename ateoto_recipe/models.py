from django.db import models
from django.template.defaultfilters import slugify

class Ingredient(models.Model):
    name = models.CharField(max_length = 50)
    slug = models.SlugField(editable = False)

    def __unicode__(self):
        return u'%s' % (self.name)

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.name)
        
        super(Ingredient, self).save(*args, **kwargs)


class IngredientLine(models.Model):
    ingredient = models.ForeignKey(Ingredient)
    quantity = models.CharField(max_length = 50)
    preparation = models.CharField(max_length = 50)

    def __unicode__(self):
        return u'%s %s (%s)' % (self.quantity, self.ingredient, self.preparation)
