import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class LikeableMixin(models.Model):
    likes = models.ManyToManyField(get_user_model(),
                                   related_name="%(app_label)s_%(class)s_like_set",
                                   related_query_name="%(app_label)s_%(class)s_likes")

    class Meta:
        abstract = True


class PublishedText(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    text = models.CharField(max_length=50000, verbose_name="Post Text Contents")
    pub_time = models.DateTimeField('Publication time', default=timezone.now)

    def __str__(self):
        return f"({self.author.username},{str(self.pub_time)},{self.text[:20]})"


class Post(LikeableMixin, PublishedText):
    pass


class Comment(LikeableMixin, PublishedText):
    parent_content = models.ForeignKey(PublishedText, on_delete=models.CASCADE, related_name='comment_set')
