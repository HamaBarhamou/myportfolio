# Generated by Django 5.0.6 on 2024-05-27 19:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0009_alter_event_description"),
    ]

    operations = [
        migrations.RenameField(
            model_name="event",
            old_name="date",
            new_name="end_date",
        ),
        migrations.AddField(
            model_name="event",
            name="start_date",
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
