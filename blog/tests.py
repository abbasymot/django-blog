from django.test import TestCase
from django.urls.base import reverse
from .models import Category, Post, Tag
# Create your tests here.

class BlogTestCase(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(
            title = "test_tag",
            slug = "test_tag_slug"
        )
        self.category = Category(
            title = "category",
            slug = "category_slug"
        )
        self.post = Post.objects.create(
            title = "post_title",
            slug = "post_slug",
            body = "post_body",
        )

    def test_slug_creation(self):
        self.assertEqual(self.tag.title, "test_tag")
        self.assertEqual(self.tag.slug, "test_tag_slug")

    def test_category_creation(self):
        self.assertEqual(self.category.title, "category")
        self.assertEqual(self.category.slug, "category_slug")

    def test_post_creation(self):
        self.assertEqual(self.post.title, "post_title")
        self.assertEqual(self.post.slug, "post_slug")
        self.assertEqual(self.post.body, "post_body")

    def test_posts_list_page(self):
        response = self.client.get(reverse("posts"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_list.html")

    def test_posts_details_page(self):
        response = self.client.get(reverse("post", kwargs={"slug": self.post.slug}))
        no_response = self.client.get(reverse("post", kwargs={"slug": 2}))
        self.assertNotEqual(no_response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_details.html")

    def test_posts_create_page(self):
        response = self.client.get(reverse("create"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "blog/post_form.html")

    def test_posts_delete_page(self):
        response = self.client.get(reverse("delete", kwargs={"slug": self.post.slug}))
        self.assertEqual(response.status_code, 302)