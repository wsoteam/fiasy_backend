from django.contrib import admin

from articles.models import Article, ArticleCategory
from modeltranslation.admin import TranslationAdmin


class ArticleCategoryAdmin(admin.ModelAdmin):
    list_select_related = ('parent',)
    list_display = ['name', 'parent']
    list_filter = ('parent',)
    search_fields = ('name', 'parent__name',)

    class Meta:
        model = ArticleCategory


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'date']
    search_fields = ('title', 'body')
    list_filter = ('category',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleCategory, ArticleCategoryAdmin)
