# Generated by Django 2.2.4 on 2019-08-01 17:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('socialnet', '0004_auto_20190731_1625'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='likes',
            field=models.ManyToManyField(related_name='socialnet_comment_like_set', related_query_name='socialnet_comment_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='socialnet_post_like_set', related_query_name='socialnet_post_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]