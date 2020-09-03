# Generated by Django 2.2.12 on 2020-08-21 20:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [("common", "0082_auto_20200821_1617")]

    operations = [
        migrations.AddField(
            model_name="repositoryintent",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
                verbose_name="created at",
            ),
            preserve_default=False,
        )
    ]
