'''
This module contains the models for the application.

The Post model reperesents a sticky note created by the user. Each post
post has a title, content, timestamp and author.
'''

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    """
    Represents a blog post with a title, content, author, and timestamp.

    Attributes:
        title (str): The title of the post.
        content (str): The content of the post.
        created_at (datetime): The date and time when the post was created.
        author (User): The user who authored the post.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
