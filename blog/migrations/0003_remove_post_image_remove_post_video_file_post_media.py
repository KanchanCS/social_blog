# Generated by Django 4.1.2 on 2022-10-04 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0002_alter_post_create_date_alter_post_updated_date"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="image",
        ),
        migrations.RemoveField(
            model_name="post",
            name="video_file",
        ),
        migrations.AddField(
            model_name="post",
            name="media",
            field=models.FileField(blank=True, null=True, upload_to="post/files"),
        ),
    ]
