from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils import formats
# Create your models here.

class LocUnit(models.Model):
    name = models.CharField(max_length=220)
    number = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    days = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)

class Event(models.Model):
    locUnit = models.ForeignKey(LocUnit, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    #date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    # rest of the fields
    #objects = CustomManager()

    def __str__(self):
        return str(self.locUnit.name)