# Generated by Django 4.2.1 on 2023-05-18 16:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("job", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="contact_number",
            field=models.IntegerField(null=True),
        ),
    ]
