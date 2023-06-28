from django.test import TestCase
from django.urls import reverse
from .models import Post

# Create your tests here.


class PostsTest(TestCase):
    """We will test:
    url exists and returns 200 status code
    url is avaliable and uses correct template
    content matches with that is expected

    In addition model works correctly

    """

    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(text="This is a test!")

    def test_model_content(self):
        self.assertEqual(self.post.text, "This is a test!")

    def test_url_existence(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_name(self):
        response = self.client.get(reverse("post-home"))
        self.assertEqual(response.status_code, 200)

    def test_url_template(self):
        response = self.client.get(reverse("post-home"))
        self.assertTemplateUsed(response, "home.html")

    def test_url_content(self):
        response = self.client.get(reverse("post-home"))
        self.assertContains(response, "<h1>Message Board Homepage</h1>")

    def test_home_page(self):
        response = self.client.get(reverse("post-home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        self.assertContains(response, "<h1>Message Board Homepage</h1>")
