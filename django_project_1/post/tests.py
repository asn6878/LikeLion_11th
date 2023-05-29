from django.test import TestCase, Client
from django.utils import timezone
from post.models import *
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your tests here.

class PostViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpassword',
        )
        self.blog = Blog.objects.create(
            title='Test Blog',
            blog_profile='This is a test blog.',
            user=self.user,
            created_time = timezone.now(),
        )
        self.category = Category.objects.create(
            name='Test Category',
            blog = self.blog,
        ) 
        self.post = Post.objects.create(
            title='Test Post',
            body='This is a test post.',
            author = self.user,
            category = self.category,
            date = timezone.now(),
        )
        self.comment = Comment.objects.create(
            author = self.user,
            post = self.post,
            comment = "This is a test comment",
        )
        self.today = Today.objects.create(
            today_day = 10000,
            today_total = 10000*10000,
            blog = self.blog
        )
        # 유효한 category_id 값을 가지는 Category 인스턴스 생성
    def test_post_list_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('post:index'))
        # assertEqual로 HttpResponse의 상태코드가 200인지ㅍ확인한다.
        self.assertEqual(response.status_code, 200)
    
    def test_post_create_view(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(reverse('post:create'))
        self.assertEqual(response.status_code, 200)

    def test_post_read_view(self):
        self.client.login(username='testuser', password='testpassword')
        post = Post.objects.all()
        response = self.client.get(reverse('post:detail', args=(post[0].id,)))
        self.assertEqual(response.status_code, 200)
        
    def test_post_delete_view(self):
        self.client.login(username='testuser', password='testpassword')
        post = Post.objects.all()
        response = self.client.get(reverse('post:delete', args=(post[0].id,)))
        self.assertEqual(response.status_code, 200)