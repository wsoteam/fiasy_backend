from django.db import models

from django.utils.translation import ugettext_lazy as _


class FeedbackType(models.Model):
    name = models.CharField(_('Name'), max_length=255, unique=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    feedback = models.CharField(
        _('Feedback'),
        max_length=255,
    )
    feedback_type = models.ForeignKey(
        FeedbackType,
        verbose_name=_("Type"),
        related_name='type',
        on_delete=models.PROTECT
    )

    def __str__(self):
        return str(self.feedback)

