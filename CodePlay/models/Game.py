import datetime
from django.db import models
from django.utils import timezone

class Start(models.Model):
    time = models.DateTimeField(default=timezone.now)

# Hold all sessions
class Result(models.Model):
    result = models.IntegerField()
    time = models.DateTimeField(default=timezone.now)
