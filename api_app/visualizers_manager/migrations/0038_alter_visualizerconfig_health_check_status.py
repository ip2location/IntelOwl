# Generated by Django 4.2.11 on 2024-04-10 09:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("visualizers_manager", "0037_4_change_primary_key"),
    ]

    operations = [
        migrations.AlterField(
            model_name="visualizerconfig",
            name="health_check_status",
            field=models.BooleanField(default=True),
        ),
    ]
