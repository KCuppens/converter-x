# Generated by Django 4.1.3 on 2022-11-27 11:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("initial_files", "0001_initial"),
        ("conversions", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="conversion",
            name="initial_file",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="initial_files.initialfile",
            ),
        ),
    ]
