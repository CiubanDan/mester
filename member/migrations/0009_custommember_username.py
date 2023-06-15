# Generated by Django 4.2.1 on 2023-05-22 17:25
import datetime
from random import random

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("member", "0008_worker_about_me"),
    ]

    operations = [
        migrations.AddField(
            model_name="custommember",
            name="username",
            field=models.CharField(
                default="general",
                error_messages={"unique": "A user with that username already exists."},
                help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                max_length=150,
                unique=True,
                validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                verbose_name="username" + str(random()),
            ),
            preserve_default=False,
        ),
    ]