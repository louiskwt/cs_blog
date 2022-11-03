from django.test import TestCase
from django.urls import reverse
from .models import Post
from django.contrib.auth.models import User

class BlogDetailTest(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = User.objects.create_user(username="testuser", password="12345")

        cls.post = Post.objects.create(title="Test", slug="test", body="hello", status=Post.Status.PUBLISHED, author=cls.user)

    def test_wrong_blog_detail_url(self):
        response = self.client.get(reverse("blogs:post_detail", kwargs={'id': 200}))
        self.assertEqual(response.status_code, 404)

    def test_correct_blog_detail_url(self):
        response = self.client.get(reverse("blogs:post_detail", kwargs={'id': self.post.id }))
    
        self.assertEqual(response.status_code, 200)
    
    def test_blog_detail_template(self):
        response = self.client.get(reverse("blogs:post_detail", kwargs={'id': self.post.id }))
        self.assertTemplateUsed(response, 'blog/detail.html')
        self.assertTemplateUsed(response, 'base.html')

