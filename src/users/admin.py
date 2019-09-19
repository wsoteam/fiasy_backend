from django.contrib import admin

from users.models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    search_fields = ('user',)
    list_select_related = ('user',)
    list_display = [
        'user',
        'image',
        'age',
        'height',
        'weight',
        'max_carbo',
        'max_fats',
        'max_calories',
        'max_proteins',
        'water_count'
    ]

    class Meta:
        model = UserProfile

admin.site.register(UserProfile, UserProfileAdmin)
