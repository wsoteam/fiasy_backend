from django.contrib import admin

from articles.models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    search_fields = ('title', 'body')

admin.site.register(Article, ArticleAdmin)
