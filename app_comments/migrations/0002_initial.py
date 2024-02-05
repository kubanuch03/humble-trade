# Generated by Django 4.2.7 on 2024-02-04 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("app_comments", "0001_initial"),
        ("app_video_library", "0001_initial"),
        ("app_clients", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="commentdocument",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app_clients.client"
            ),
        ),
        migrations.AddField(
            model_name="commentcourse",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="app_video_library.courses",
            ),
        ),
        migrations.AddField(
            model_name="commentcourse",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app_clients.client"
            ),
        ),
    ]