__author__ = 'rd'

from django.contrib import admin

from RBE.main.models import Post, Comment, Tag

admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)
