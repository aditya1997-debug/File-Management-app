# Generated by Django 5.0.4 on 2024-04-21 11:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("file_manager", "0006_folder_files"),
    ]

    operations = [
        migrations.AlterField(
            model_name="file",
            name="file",
            field=models.FileField(upload_to="uploaded_files/"),
        ),
    ]