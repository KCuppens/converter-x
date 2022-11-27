# Generated by Django 4.1.3 on 2022-11-22 17:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("config_file", "0001_initial"),
        ("compression", "0002_compression_initial_file"),
        ("action", "0002_remove_action_compressions_action_compressions"),
    ]

    operations = [
        migrations.AddField(
            model_name="action",
            name="config_file",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="config_file.configfile",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="action",
            name="compressions",
            field=models.ManyToManyField(blank=True, to="compression.compression"),
        ),
    ]
