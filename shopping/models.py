from django.db import models
from datetime import datetime

class PlanToBuy(models.Model):
    ''' Contains the weekend plans. '''
    added = models.DateTimeField(
            default=datetime.now,
            )
    name = models.CharField(
            max_length = 200,
            unique=True,
            )
    expected_purchase_date = models.DateTimeField(
            default=None,
            blank=True,
            null=True,
            )
    bought = models.DateTimeField(
            default=None,
            blank=True,
            null=True,
            )
