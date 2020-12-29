from django.db import models

# Create your models here.
class TeamDict(models.Model):
    teamNames = models.CharField(max_length=500)
    predictions = models.CharField(max_length=500)
