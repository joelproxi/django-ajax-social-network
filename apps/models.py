from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class CreationModificationMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True
        ordering = ('-created_at',)
        indexes = [
            models.Index(fields=['-created_at'])
        ]


class Post(CreationModificationMixin):
    content = models.TextField(null=True, blank=True)
    # slug = models.SlugField(max_length=500, unique=True)
    # image = models.ImageField(upload_to='images/post')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    users_like = models.ManyToManyField(User, related_name='user_like_post', through='LikePost')
    
    class Meta(CreationModificationMixin.Meta):
        pass


class Media(models.Model):
    post = models.ForeignKey(Post, 
                             on_delete=models.CASCADE, 
                             related_name="post_media")
    image = models.ImageField(upload_to='images/post/')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        pass
    
    
class Comment(CreationModificationMixin):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comment')
    content = models.CharField(max_length=500)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posted')
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    users_like = models.ManyToManyField(User, related_name='user_like_comment', through='LikeComment')
    
    class Meta(CreationModificationMixin.Meta):
        pass
    
    def __str__(self) -> str:
        return self.content
        

class LikePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_like')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        pass


class LikeComment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_like')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment_user')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        pass
    
           
class Follow(models.Model):
    user_from = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_set')
    user_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_to')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "%s started follow %s" % (self.user_from.get_username, self.user_to.get_username)
    

User.add_to_class('follow_user',
                  models.ManyToManyField('self', related_name='followed', symmetrical=False))