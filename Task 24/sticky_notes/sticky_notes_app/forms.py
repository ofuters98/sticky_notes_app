'''
This module contains the forms that used in the sticky notes
application.

The PostForm is a form that will allow users to create a new post. It
will have the fields for the title and the content of the post.

The form is used in the views to handle any user input for creating a
post
'''

from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    '''
    This class will create a form where the user will be able to make
    a new post. It will use the Post model to do this and will require
    the user to enter a title and the main body of content.
    '''
    class Meta:
        model = Post
        fields = ['title', 'content']
