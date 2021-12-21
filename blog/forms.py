from django.db.models.base import Model
from django.forms import ModelForm
from django import forms
from .models import Post


class PostForm(ModelForm):
    """
    A form to create a new post
    """
    class Meta:
        author = forms.CharField()
        slug = forms.SlugField()
        model = Post
        fields = ["title", "thumbnail", "description", "body", "tag", "category", "status"]


    