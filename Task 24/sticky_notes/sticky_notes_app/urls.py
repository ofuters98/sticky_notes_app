from django.urls import path
from . import views

urlpatterns = [
    # Points to the signup page.
    path('signup/', views.signup_view, name='signup'),
    # Points to the posts_list page.
    path('posts/', views.posts_list, name='posts_list'),
    # Points to each individual post using the primary key (pk) which
    # will be displayed in the URL.
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # Points to the create post page.
    path('create_post/', views.create_post, name='create_post'),
    # Points to the delete post view.
    path('post/<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('post/<int:pk>/edit/', views.edit_post, name='edit_post'),
]
