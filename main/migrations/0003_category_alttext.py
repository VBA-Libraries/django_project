# Generated by Django 3.2.8 on 2022-06-19 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220620_0051'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='altText',
            field=models.TextField(blank=True, null=True),
        ),
    ]
