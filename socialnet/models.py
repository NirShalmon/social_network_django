import datetime

from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.db import models
from django.utils import timezone


class PublishedText(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    text = models.CharField(max_length=50000, verbose_name="Post Text Contents")
    pub_time = models.DateTimeField('Publication time', default=timezone.now)
    likes = models.ManyToManyField(get_user_model(),
                                   related_name="%(app_label)s_%(class)s_like_set",
                                   related_query_name="%(app_label)s_%(class)s_likes")

    def __str__(self):
        return f"({self.author.username},{str(self.pub_time)},{self.text[:20]})"


class Post(PublishedText):
    pass


class Comment(PublishedText):
    parent_content = models.ForeignKey(PublishedText, on_delete=models.CASCADE, related_name='comment_set')
