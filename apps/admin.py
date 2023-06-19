
from django.contrib import admin

from apps.models import Comment, Follow, LikePost, Notification, Post

# Register your models here.

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(LikePost)
admin.site.register(Notification)
admin.site.register(Follow)
