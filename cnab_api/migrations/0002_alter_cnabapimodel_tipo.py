# Generated by Django 4.1.5 on 2023-01-25 18:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cnab_api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="cnabapimodel",
            name="tipo",
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1),
                    django.core.validators.MaxValueValidator(9),
                ]
            ),
        ),
    ]
