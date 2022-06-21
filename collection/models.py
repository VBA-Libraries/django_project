from pyexpat import model
from django.db import models

# Create your models here.


class Collection(models.Model):
    name = models.CharField(null=True, blank=True, max_length=200)
    amount = models.DecimalField(
        null=True, blank=False, decimal_places=2, max_digits=10)
    date_created = models.DateTimeField(blank=True, null=True)
