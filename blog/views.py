from django.http import request
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Comment, Post
from users.models import Profile
from .forms import PostForm


class PostListView(ListView):
    """
    Return all of the posts
    """
    model = Post
    ordering = '-created' 
    context_object_name = 'posts'
    template_name ='blog/post_list.html'


def post_details(request, slug):
    """
    Return Single post details
    """
    post = get_object_or_404(Post, slug=slug)
    comments = get_list_or_404(Comment, post=post)
    context = {"post": post,"comments": comments}
    return render(request, 'blog/post_details.html', context)


def post_create(request):
    """
    Create a new post
    """
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the corrently logedin user.
            profile = Profile.objects.get(user=request.user.id) 
            post = form.save(commit=False)
            # Set the post author to profile.
            post.author = profile 
            # Set the slug based on title.
            post.slug = slugify(post.title)
            post.save()
            return redirect(post.get_absolute_url())
    context = {'form': form}
    return render (request, 'blog/post_form.html', context)


def  post_update(request, slug):
    """
    Update a post
    """
    post = Post.objects.get(slug=slug) # Get the post
    profile = Profile.objects.get(user=request.user)
    form = PostForm(instance=post)
    if post.author == profile: # If logged in user is author of the post
        if request.method == 'POST':
            form = PostForm(request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                return redirect(post.get_absolute_url())
    else:
        return redirect("posts")
    context = {"form": form}
    return render(request, 'blog/post_form.html',context)
                
        
class PostDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete a post
    """
    model = Post
    context_object_name = 'post'
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy("posts")


class SearchListView(ListView):
    """
    Search in posts
    """
    model = Post
    context_object_name="posts"
    ordering = '-created' 
    template_name ='blog/post_list.html'

    def get_queryset(self):
        query = self.request.GET.get("q")
        print(query)
        return Post.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
            | Q(body__icontains=query)
        )

    