# Generated by Django 2.2.1 on 2019-07-31 12:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('socialnet', '0002_auto_20190731_1251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='Publication time',
        ),
        migrations.RemoveField(
            model_name='post',
            name='Publication time',
        ),
        migrations.AddField(
            model_name='comment',
            name='pub_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Publication time'),
        ),
        migrations.AddField(
            model_name='post',
            name='pub_time',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Publication time'),
        ),
    ]
