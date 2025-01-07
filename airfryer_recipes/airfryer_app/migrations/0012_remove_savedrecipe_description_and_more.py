# Generated by Django 5.1.4 on 2024-12-22 11:56

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("airfryer_app", "0011_auto_20241222_1152"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="savedrecipe",
            name="description",
        ),
        migrations.AddField(
            model_name="savedrecipe",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
