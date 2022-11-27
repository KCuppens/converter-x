# Generated by Django 4.1 on 2022-10-30 06:23

import uuid

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Page",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Unique identification",
                    ),
                ),
                (
                    "date_created",
                    models.DateTimeField(auto_now=True, verbose_name="Date of creation"),
                ),
                (
                    "date_published",
                    models.DateTimeField(
                        blank=True,
                        default=django.utils.timezone.now,
                        null=True,
                        verbose_name="Publishingdate",
                    ),
                ),
                (
                    "date_expired",
                    models.DateTimeField(blank=True, null=True, verbose_name="Expiring date"),
                ),
                (
                    "date_updated",
                    models.DateTimeField(auto_now=True, verbose_name="Date of last update"),
                ),
                (
                    "date_deleted",
                    models.DateTimeField(blank=True, null=True, verbose_name="Delete date"),
                ),
                (
                    "state",
                    models.CharField(
                        choices=[
                            ("draft", "Draft"),
                            ("in review", "In review"),
                            ("published", "Published"),
                            ("changes requested", "Changes requested"),
                            ("schedule", "Schedule"),
                        ],
                        default="draft",
                        max_length=255,
                    ),
                ),
                (
                    "key_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "title",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("content", models.TextField(blank=True)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
