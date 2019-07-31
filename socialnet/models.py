import datetime

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone


class PublishedText(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    text = models.CharField(max_length=50000, verbose_name="Post Text Contents")
    pub_time = models.DateTimeField('Publication time', default=timezone.now)

    class Meta:
        abstract = True

    def __str__(self):
        return f"({self.author.username},{str(self.pub_time)},{self.text[:20]})"


class Post(PublishedText):
    pass


class Comment(PublishedText):
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
