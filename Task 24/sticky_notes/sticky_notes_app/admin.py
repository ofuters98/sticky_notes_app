from django.contrib import admin
from .models import Post

# Register your models here.

# Allows a super user to view any posts, edit or delete them as well as
# create new posts from the django admin interface.
admin.site.register(Post)
