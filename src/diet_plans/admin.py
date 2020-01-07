from django.contrib import admin
from diet_plans.models import DietPlan, DayInPlan, DietPlanCategory
from recipes.models import Recipe


class DietPlanCategoryAdmin(admin.ModelAdmin):
    list_select_related = ('parent',)
    list_display = ['name', 'parent']
    list_filter = ('parent',)
    search_fields = ('name', 'parent__name',)

    class Meta:
        model = DietPlanCategory


class RecipeInlineAdmin(admin.TabularInline):
    model = DayInPlan
    extra = 1


class DietPlanAdmin(admin.ModelAdmin):
    list_display = ['name']
    inlines = [RecipeInlineAdmin]


admin.site.register(DietPlan, DietPlanAdmin)
admin.site.register(DietPlanCategory, DietPlanCategoryAdmin)
