# Generated by Django 4.2.7 on 2023-11-30 18:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("customer", "0003_alter_servicelocation_zipcode"),
    ]

    operations = [
        migrations.CreateModel(
            name="DeviceModel",
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
                    "model_name",
                    models.CharField(max_length=20, verbose_name="ModelName"),
                ),
                (
                    "device_type",
                    models.CharField(max_length=30, verbose_name="DeviceType"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EnergyPrice",
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
                    "zipcode",
                    models.CharField(
                        default="00000",
                        help_text="Enter the zipcode",
                        validators=[django.core.validators.MinLengthValidator(5)],
                        verbose_name="ZipCode",
                    ),
                ),
                (
                    "time_stamp",
                    models.DateTimeField(auto_now=True, verbose_name="TimeStamp"),
                ),
                (
                    "price_per_unit",
                    models.FloatField(
                        validators=[django.core.validators.MinValueValidator(0.1)],
                        verbose_name="PricePerUnit",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EnrolledDevice",
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
                    "device_model",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="device.devicemodel",
                    ),
                ),
                (
                    "location",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="customer.servicelocation",
                    ),
                ),
            ],
        ),
    ]
