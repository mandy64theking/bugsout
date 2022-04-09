from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title = models.TextField(max_length=100,null=True)
    description = models.TextField(null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    #@property
   # def number_of_comments(self):
     #   return Comment.objects.filter(post_connected=self).count()
class Comment(models.Model):
    text=models.TextField(null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
    post_connected = models.ForeignKey(Post, on_delete=models.CASCADE)