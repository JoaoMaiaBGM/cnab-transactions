# Generated by Django 4.1.5 on 2023-01-25 18:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CnabApiModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "tipo",
                    models.IntegerField(
                        max_length=1,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(9),
                        ],
                    ),
                ),
                ("data", models.DateField()),
                ("valor", models.DecimalField(decimal_places=2, max_digits=10)),
                ("cpf", models.CharField(max_length=11)),
                ("cartao", models.CharField(max_length=12)),
                ("hora", models.TimeField()),
                ("dono_da_loja", models.CharField(max_length=14)),
                ("nome_loja", models.CharField(max_length=19)),
            ],
        ),
    ]