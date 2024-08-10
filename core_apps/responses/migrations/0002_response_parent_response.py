# Generated by Django 4.1.7 on 2024-08-10 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("responses", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="response",
            name="parent_response",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="replies",
                to="responses.response",
            ),
        ),
    ]
