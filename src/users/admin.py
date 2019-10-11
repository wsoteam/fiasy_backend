from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User, Group

from users.models import UserProfile


class UserProfileAdmin(admin.StackedInline):
    model = UserProfile
    # list_display = [
    #     'id'
    #     'image',
    #     'age',
    #     'height',
    #     'weight',
    #     'max_carbo',
    #     'max_fats',
    #     'max_calories',
    #     'max_proteins',
    #     'water_count'
    # ]


class UserAdmin(UserAdmin):
    inlines = [
        UserProfileAdmin
    ]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
