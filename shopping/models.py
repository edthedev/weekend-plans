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
    plan_to_buy = models.DateTimeField(
            default=None,
            blank=True,
            null=True,
            )
    bought = models.DateTimeField(
            default=None,
            blank=True,
            null=True,
            )
