# Generated by Django 4.2 on 2023-04-12 11:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("games", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="game",
            name="date_created",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
