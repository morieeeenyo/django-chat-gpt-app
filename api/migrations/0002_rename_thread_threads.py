# Generated by Django 4.2.9 on 2024-01-14 01:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Thread",
            new_name="Threads",
        ),
    ]
