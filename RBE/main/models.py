# -*- coding: utf-8 -*-
from django.db import models


class Post(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(blank=False, max_length=255)
    text = models.TextField(blank=False)


class Comment(models.Model):
    text = models.TextField(blank=False)
    to_post = models.ForeignKey(Post, related_name='comments')


class Tag(models.Model):
    text = models.CharField(blank=False, max_length=255)
    posts = models.ManyToManyField(Post, related_name='tags')
