# Generated by Django 4.2.1 on 2023-05-23 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("member", "0010_remove_custommember_username"),
    ]

    operations = [
        migrations.AlterField(
            model_name="worker",
            name="member",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="worker",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]