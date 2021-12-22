from django.db import models
from django.urls import reverse
from users.models import Profile


class Tag(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Post(models.Model):
    STATUS_CHOICES = [
        ('p', 'Publish'),
        ('d', 'Draft')
    ]
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    thumbnail = models.ImageField(upload_to='images/thumbnails/%Y/%m/%d/', default='images/thumbnails/default.jpg')
    description = models.TextField(max_length=400, blank=True, null=True)
    body = models.TextField()
    tag = models.ManyToManyField(Tag, related_name="tags")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='p')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post", kwargs={'slug': self.slug})


class Comment(models.Model):
    STATUS_CHOICES = [
        ('p', 'Publish'),
        ('d', 'Draft')
    ]
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=2000)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='p')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title