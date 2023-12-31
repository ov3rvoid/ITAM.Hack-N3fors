# Generated by Django 4.1.7 on 2023-08-21 18:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="calculation",
            name="updated_at",
        ),
        migrations.AlterField(
            model_name="calculation",
            name="A_max",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="calculation",
            name="A_min",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="calculation",
            name="dB",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="telegramuser",
            name="external_id",
            field=models.BigIntegerField(unique=True, verbose_name="tg id"),
        ),
    ]
