'''
This django application allows users to create and and view sticky
notes / posts. Users will be able to sign up for an account, log in to
an existing account, create a new post, delete their own posts, update
their own posts and view other users' posts.

Every post will have a title, content, timestamp and
author. The title, timestamp and author of each post will be displayed
to the user as a list in reverse chronological order as soon as they are
logged in. They can then click each post to view its content.

When viewing a post in detail, if the logged in user is the same as the
author, a button will appear which will allow them to delete the post as
well as one to update the post. Only the author of the post or a
superuser (via the django admin panel) will be able to delete or update
posts.

A superuser will also be able to create and delete accounts from the
django admin panel.
'''

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Post
from .forms import PostForm


# Create your views here.
def login_view(request):
    '''
    This function will let the user log in and then take them to the
    posts_list page if they do so succesfully. It will use djangos built
    in authentication form to check the users log in details are correct
    before loging them in.
    '''
    # If the request was a post request and the form was filled out
    # correctly, log the user in and take them to the posts list.
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('posts_list')
    # Otherwise, display the form (I.E. the log in page)
    else:
        form = AuthenticationForm()
    return render(request, 'sticky_notes_app/login.html', {'form': form})


def signup_view(request):
    '''
    This method will create a new user. Once a new user has been
    created successfully, they'll be redirected to the posts list. It
    will use djangos built in user creation form to build this new user
    account.
    '''
    # If the request was a post request and the form was filled out
    # correctly, use these new log in details to log the user in and
    # take them to the posts list. Also, save these log in details to
    # the database.
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('posts_list')
    # Otherwise, display the form (I.E. the signup page)
    else:
        form = UserCreationForm()
    return render(request, 'sticky_notes_app/signup.html', {'form': form})


@login_required
def logout_view(request):
    '''
    When the user is logged in, they have the option to log out. When
    they do this, they are redirected back to the login page.
    '''
    logout(request)
    return redirect('login')


@login_required
def posts_list(request):
    '''
    This function will form and display all of the posts that have
    previously been added in reverse chronilogical order.
    '''
    posts = Post.objects.order_by('-created_at')
    # Renders the page using the posts_list.html
    return render(request, 'sticky_notes_app/posts_list.html',
                  {'posts': posts})


@login_required
def post_detail(request, pk):
    '''
    This function will display a post in full when the user selects it.
    It will do this using the primary key.
    '''
    # Use the primary key to retrieve a post. If the post can't be found
    # then raise an error 404.
    post = get_object_or_404(Post, pk=pk)
    # Renders the page using the post_detail.html
    return render(request, 'sticky_notes_app/post_detail.html', {'post': post})


@login_required
def create_post(request):
    '''
    This method will allow a user to create a new post. It will use our
    PostForm to take in the title and main body from the user. Each post
    will also be added to the database.
    '''
    # If the request method was a post request and the form was filled
    # out correctly, find the user who filled out the form and make them
    # the author and then save the post to the database. Then take the
    # user back to the posts_list.
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            return redirect('posts_list')
    # Otherwise, display the form (I.E. the create_post page)
    else:
        form = PostForm()
    return render(request, 'sticky_notes_app/create_post.html', {'form': form})


@login_required
def delete_post(request, pk):
    '''
    This method will allow a user to delete a post. It will first check
    that the user is the person who made the post in the first place
    and then will allow them to delete it if this is the case.'''
    # Use the primary key to retrieve a post. If the post can't be found
    # then raise an error 404.
    post = get_object_or_404(Post, pk=pk)
    # If the post author is the same as the current user then delete
    # the post and go back to the posts_list page.
    if post.author == request.user:
        post.delete()
        return redirect('posts_list')
    return redirect('post_detail', pk=pk)


@login_required
def edit_post(request, pk):
    '''
    This method will allow a user to edit their won posts. The button
    to update the post will only appear if the post author matches the
    logged in user.'''
    # Use the primary key to retrieve a post. If the post can't be found
    # then raise an error 404.
    post = get_object_or_404(Post, pk=pk, author=request.user)
    # If the request method was a post request and the form was filled
    # out correctly, then change make any changes post and save these.
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'sticky_notes_app/edit_post.html',
                  {'form': form, 'post': post})
