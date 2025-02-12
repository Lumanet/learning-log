# Generated by Django 5.0.7 on 2024-07-19 17:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("learning_logs", "0003_topic_owner"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="entry",
            name="topic",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="entradas",
                to="learning_logs.topic",
            ),
        ),
        migrations.AlterField(
            model_name="topic",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="temas",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
