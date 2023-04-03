
from django.contrib import admin

from apps.models import Comment, LikePost, Post

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(LikePost)
