from django.db import models

# Create your models here.


class Expense(models.Model):
    item_name = models.CharField(null=True, blank=True, max_length=200)
    item_amount = models.CharField(null=True, blank=True, max_length=200)
    item_category = models.CharField(null=True, blank=True, max_length=200)
    expense_date = models.DateField()

    def __str__(self):
        return self.item_name
