# Generated by Django 4.2.1 on 2023-05-23 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("member", "0010_remove_custommember_username"),
        ("job", "0003_alter_job_worker"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="category_type",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="member.category",
            ),
        ),
    ]
