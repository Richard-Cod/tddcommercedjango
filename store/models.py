from django.db import models

from tddCommerce import settings
# Create your models here.


class Customer(models.Model):
    DIAMOND = 'D'
    GOLD = 'G'
    SILVER = 'S'
    SUBSCRIPTION_TYPES = (
        (DIAMOND, 'Diamond'),
        (GOLD, 'Gold'),
        (SILVER, 'Silver'),
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    subscription = models.CharField(
        max_length=1, choices=SUBSCRIPTION_TYPES, default=SILVER)
