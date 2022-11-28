# Generated by Django 4.1.3 on 2022-11-28 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("conversions", "0003_conversion_converted_file"),
    ]

    operations = [
        migrations.AddField(
            model_name="conversion",
            name="from_action",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="conversion",
            name="status",
            field=models.CharField(
                choices=[
                    ("open", "Open"),
                    ("pending", "Pending"),
                    ("closed", "Closed"),
                ],
                default="open",
                max_length=255,
            ),
        ),
        migrations.AddField(
            model_name="conversion",
            name="to_action",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]