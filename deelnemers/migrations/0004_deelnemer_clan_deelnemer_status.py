# Generated by Django 5.2.1 on 2025-05-28 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("deelnemers", "0003_deelnemer_foto"),
    ]

    operations = [
        migrations.AddField(
            model_name="deelnemer",
            name="clan",
            field=models.CharField(default="Geen clan", max_length=64),
        ),
        migrations.AddField(
            model_name="deelnemer",
            name="status",
            field=models.CharField(default="Actief", max_length=64),
        ),
    ]
