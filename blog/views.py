from django.http import request
from django.shortcuts import get_list_or_404, get_object_or_404, render, redirect
from django.utils.text import slugify
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models import Q

from .models import Comment, Post, Category
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

    def get_queryset(self):
        qs = Post.objects.all().order_by('-created') # All of the posts
        if self.kwargs.get('slug'): # If request has a category slug
            category_slug = self.kwargs.get('slug') # get the category slug
            category = Category.objects.get(slug = category_slug) # find the category bu slug
            category_id = Category.objects.get(id = category.id) # find the category id for filtering posts
            qs = Post.objects.filter(category = category_id).order_by('-created') # filter post that related to the category
        return qs

def post_details(request, slug):
    """
    Return Single post details
    """
    post = get_object_or_404(Post, slug=slug)
    post_comments = Comment.objects.filter(post=post)
    context = {"post": post, "comments": post_comments}
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
                
        
def post_delete(request, slug):
    profile = Profile.objects.get(user = request.user)
    post = get_object_or_404(Post, slug=slug)
    if post.author != profile:
        return redirect("posts")
    if request.method == 'POST':
        post.delete()
        return redirect("posts")
    context = {'post': post, 'profile': profile.slug}
    return render(request, "blog/post_delete.html", context)

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
        return Post.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query)
            | Q(body__icontains=query)
        )