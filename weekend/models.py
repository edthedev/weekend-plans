from django.db import models

# Create your models here.

class WeekendPlan(models.Model):
    ''' Contains the weekend plans. '''
    what_to_do = models.CharField(max_length = 200)
    when = models.CharField(max_length = 50)
