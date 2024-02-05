# Generated by Django 4.2.7 on 2024-02-05 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("app_clients", "0001_initial"),
        ("app_comment", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app_clients.client"
            ),
        ),
    ]
