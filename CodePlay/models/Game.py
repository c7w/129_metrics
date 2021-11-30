import datetime
from django.db import models

class Start(models.Model):
    time = models.DateTimeField(default=datetime.datetime.now())

# Hold all sessions
class Result(models.Model):
    result = models.IntegerField()
    time = models.DateTimeField(default=datetime.datetime.now())
