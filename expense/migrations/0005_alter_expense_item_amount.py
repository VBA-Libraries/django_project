# Generated by Django 4.0.5 on 2022-06-22 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0004_alter_expense_item_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='item_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]