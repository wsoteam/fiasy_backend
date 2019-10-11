from django.db import models
from django.contrib.auth.models import User

from django.utils.translation import ugettext_lazy as _


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    kind = models.CharField(_('Kind'), max_length=100)
    start_time_millis = models.BigIntegerField(_('Start Time'))
    expiry_time_millis = models.BigIntegerField(_('Expiry Time'))
    auto_renewing = models.BooleanField(_('Auto Renewing'))
    price_currency_code = models.CharField(
        _('Price Currency Code'),
        max_length=5
    )
    price_amount_micros = models.BigIntegerField(_('Price Amount'))
    country_code = models.CharField(_('Country Code'), max_length=5)
    """
    The reason why a subscription was canceled or is not auto-renewing.
    Possible values are:
    0 - User canceled the subscription
    1 - Subscription was canceled by the system,
        for example because of a billing problem
    2 - Subscription was replaced with a new subscription
    3 - Subscription was canceled by the developer
    """
    cancel_reason = models.IntegerField(_('Cancel Reason'))
    order_id = models.CharField(_('Order ID'), max_length=100)
    """
    The acknowledgement state of the subscription product. Possible values are:
    0 - Yet to be acknowledged
    1 - Acknowledged
    """
    acknowledgement_state = models.IntegerField(_('Cancel Reason'))
