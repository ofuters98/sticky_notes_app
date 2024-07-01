from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Post


class StickyNotesAppTests(TestCase):

    def setUp(self):
        '''
        This method will allow us to quickly create tasks and users for
        our test. It forms part of the arrange section of the unittests.
        '''
        # Create a user
        self.user = User.objects.create_user(username='testuser',
                                             password='password')
        self.user.save()

        # Create a superuser
        self.superuser = User.objects.create_superuser(username='admin',
                                                    password='adminpassword')
        self.superuser.save()

        # Create a post
        self.post = Post.objects.create(title='Test Post',
                                        content='This is a test post.',
                                        author=self.user)

    def test_signup(self):
        '''
        Tests that users can successfully be created. The reverse
        function will generate the URL for the signup view.
        '''
        # Act
        response = self.client.post(reverse('signup'), {
            'username': 'newuser',
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        })
        # Assert
        self.assertTrue(User.objects.filter(username='newuser').exists())

    def test_create_post(self):
        '''
        Tests that posts can successfully be created.The reverse
        function will generate the URL for the create_posts view.
        '''
        # Arrange
        self.client.login(username='testuser', password='password')
        # Act
        response = self.client.post(reverse('create_post'), {
            'title': 'Another Test Post',
            'content': 'This is another test post.'
        })
        # Assert
        self.assertTrue(Post.objects.filter(
            title='Another Test Post').exists())

    def test_posts_list(self):
        '''
        Tests that the posts list is created when a user is logged in.
        The reverse function will generate the URL for the posts_list
        view.
        '''
        # Arrange
        self.client.login(username='testuser', password='password')
        # Act
        response = self.client.get(reverse('posts_list'))
        # Assert
        self.assertContains(response, 'Test Post')

    def test_post_detail(self):
        '''
        Tests that the full post will be displayed when it is required
        to do so. The reverse function will generate the URL for the
        post_detail view.
        '''
        # Arrange
        self.client.login(username='testuser', password='password')
        # Act
        response = self.client.get(reverse('post_detail', args=[self.post.pk]))
        # Assert
        self.assertContains(response, 'This is a test post.')
