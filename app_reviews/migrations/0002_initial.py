# Generated by Django 4.2.7 on 2024-02-08 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("app_reviews", "0001_initial"),
        ("app_clients", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="review",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app_clients.client"
            ),
        ),
    ]
