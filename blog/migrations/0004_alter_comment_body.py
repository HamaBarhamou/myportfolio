# Generated by Django 5.0.6 on 2024-05-28 13:52

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_tag_comment_post_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="body",
            field=ckeditor.fields.RichTextField(),
        ),
    ]
