from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, View

from .models import Profile
from blog.models import Post
# Create your views here.

@login_required()
def profile(request, slug):
    profile = Profile.objects.get(slug=slug)
    posts = Post.objects.filter(author=profile).order_by("-created")
    context = {"profile": profile, "posts": posts}
    return render(request, 'users/profile.html', context)


class ProfileUpdateView(UpdateView):
    model = Profile
    fields = ['first_name', 'last_name', 'avatar', 'about', 'location',
        'instagram', 'twitter', 'linkedin', 'website', 'is_active']
    template_name = 'users/profile_update.html'
    