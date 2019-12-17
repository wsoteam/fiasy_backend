from django.contrib import admin

from feedbacks.models import FeedbackType, Feedback

class FeedbackAdmin(admin.ModelAdmin):
    model = Feedback
    list_display = [
        'id',
        'feedback_type',
        'feedback',
    ]

    list_filter = [
        'feedback_type',
        'feedback'
    ]

admin.site.register(FeedbackType)
admin.site.register(Feedback, FeedbackAdmin)
