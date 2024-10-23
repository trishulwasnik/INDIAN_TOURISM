from django.db import models

# Create your models here.
class ANDAMAN_MODEL(models.Model):
    DURATION=models.CharField(max_length=100)
    HOTELS = models.CharField(max_length=100)
    BUDGET = models.BigIntegerField()
    CITIES = models.CharField(max_length=100)