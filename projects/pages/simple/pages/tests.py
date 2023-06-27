from django.test import SimpleTestCase
from django.urls import reverse

# Create your tests here


class HomePageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/")
        self.assertEquals(response.status_code, 200)

    def test_url_name_match(self):
        response = self.client.get(reverse("pages-home"))
        self.assertEquals(response.status_code, 200)

    def test_template_name(self):
        response = self.client.get(reverse("pages-home"))
        self.assertTemplateUsed(response, "home.html")

    def test_template_content(self):
        response = self.client.get(reverse("pages-home"))
        self.assertContains(response, "<h1>Homepage</h1>")


class AboutPageTests(SimpleTestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get("/about")
        self.assertEquals(response.status_code, 200)

    def test_url_name_match(self):
        response = self.client.get(reverse("pages-about"))
        self.assertEquals(response.status_code, 200)

    def test_template_name(self):
        response = self.client.get(reverse("pages-about"))
        self.assertTemplateUsed(response, "about.html")

    def test_template_content(self):
        response = self.client.get(reverse("pages-about"))
        self.assertContains(response, "<h1>About Page</h1>")
