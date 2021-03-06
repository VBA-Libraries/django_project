# Generated by Django 3.2.8 on 2022-06-20 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='item_amount',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='item_category',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='expense',
            name='item_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
