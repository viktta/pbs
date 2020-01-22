from django.db import models

from django.contrib.auth.models import User
from django.db import models
from django.db.models import TextField


class Registration(models.Model):
    acc = models.CharField(max_length=50)
    pas = models.CharField(max_length=50)


class Blog(models.Model):
    blog_date = models.DateTimeField('Date time')
    post = models.TextField(blank=True)
    author = models.CharField(max_length=50, blank=True)
    def __str__(self):
        return self.post



    def __int__(self):
        return self.total_posts