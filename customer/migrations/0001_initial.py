# Generated by Django 4.2.7 on 2023-11-30 17:40

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ServiceLocation",
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
                    "apt_unit",
                    models.IntegerField(
                        default=1,
                        help_text="Enter the Apartment unit of the building",
                        validators=[django.core.validators.MinValueValidator(1)],
                        verbose_name="AptUnit",
                    ),
                ),
                ("street", models.CharField(max_length=50, verbose_name="Street Name")),
                ("state", models.CharField(max_length=20, verbose_name="State Name")),
                (
                    "zipcode",
                    models.IntegerField(
                        default="00000",
                        help_text="Enter the zipcode",
                        max_length=5,
                        validators=[django.core.validators.MinLengthValidator(5)],
                        verbose_name="ZipCode",
                    ),
                ),
                ("apt_name", models.CharField(max_length=100, verbose_name="AptName")),
                ("move_in_date", models.DateField(verbose_name="MoveInDate")),
                (
                    "area",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(100)],
                        verbose_name="SquareFootage",
                    ),
                ),
                (
                    "bedroom",
                    models.IntegerField(
                        default=1,
                        validators=[django.core.validators.MinValueValidator(1)],
                        verbose_name="No of bedrooms",
                    ),
                ),
                ("occupants", models.IntegerField(verbose_name="No of occupants")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
