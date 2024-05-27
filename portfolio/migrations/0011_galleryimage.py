# Generated by Django 5.0.6 on 2024-05-27 20:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0010_rename_date_event_end_date_event_start_date"),
    ]

    operations = [
        migrations.CreateModel(
            name="GalleryImage",
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
                ("image", models.ImageField(upload_to="gallery/")),
                ("caption", models.CharField(blank=True, max_length=200)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="gallery_images",
                        to="portfolio.event",
                    ),
                ),
            ],
        ),
    ]