from django.db import models
from django.utils.translation import ugettext_lazy as _

from recipes.models import Recipe
from products.models import Category


class DietPlanCategory(Category):

    class Meta:
        verbose_name = _('Diet plan category')
        verbose_name_plural = _('Diet plan categories')


class DietPlan(models.Model):
    name = models.CharField(_("Name"), max_length=80, null=True, unique=True)
    category = models.ForeignKey(
        DietPlanCategory,
        verbose_name=_("Category"),
        null=True,
        related_name='diet_plans',
        on_delete=models.PROTECT
    )
    full_info = models.TextField(_('Full info'), blank=True)
    image = models.ImageField(
        _('Image'),
        upload_to='article_image',
        blank=True
    )
    total_days = models.IntegerField(
        _('Total Days in Plan'),
        choices=((int(x), x) for x in range(1, 32)),
        blank=True,
        null=True,
    )
    premium = models.BooleanField(_('Premium'), default=True)
    recipes = models.ManyToManyField(
        Recipe,
        verbose_name=_("Recipe"),
        blank=True,
        through='DayInPlan',
        related_name='recipes'
    )

    def __str__(self):
        return self.name


class DayInPlan(models.Model):
    diet_plan = models.ForeignKey(
        DietPlan,
        related_name='day',
        on_delete=models.PROTECT
    )
    recipe = models.ForeignKey(
        Recipe,
        blank=True,
        null=True,
        related_name='day',
        on_delete=models.PROTECT
    )
    day = models.IntegerField(
        _('Day in diet plan'),
        choices=((int(x), x) for x in range(1, 32)),
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.day)
