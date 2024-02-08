# Generated by Django 4.2.7 on 2024-02-08 09:04

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("title", models.CharField(max_length=250, unique=True)),
                ("image", models.ImageField(upload_to="resourse/category/")),
            ],
        ),
        migrations.CreateModel(
            name="Document",
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
                ("title", models.CharField(max_length=250)),
                (
                    "image",
                    models.ImageField(upload_to="", verbose_name="resourse/document/"),
                ),
                ("post", models.FileField(upload_to="")),
                ("url", models.URLField()),
                ("description", models.CharField(max_length=250)),
            ],
        ),
    ]
