from django.contrib import admin

from .models import ActivityTime, Activity, CustomUserActivity

from import_export import resources
from import_export.admin import ImportExportModelAdmin, ExportActionMixin


class ActivityResource(resources.ModelResource):
    class Meta:
        model = Activity
        import_id_fields = ['id']

        fields = (
            'id',
            'name',
            'сonsumption'
        )


class ActivityTimeInlineAdmin(admin.TabularInline):
    model = ActivityTime
    extra = 1


class ActivityAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ['name']
    inlines = [ActivityTimeInlineAdmin]
    resource_class = ActivityResource


admin.site.register(Activity, ActivityAdmin)
admin.site.register(CustomUserActivity)
