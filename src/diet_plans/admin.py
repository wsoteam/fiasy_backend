from django.contrib import admin

from diet_plans.models import DietPlan, DayInPlan, DietPlanCategory
from recipes.models import Recipe


class RecipeInlineAdmin(admin.TabularInline):
    model = DayInPlan
    extra = 1


class DietPlanAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [RecipeInlineAdmin]


admin.site.register(DietPlan, DietPlanAdmin)
admin.site.register(DietPlanCategory)
