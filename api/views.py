
from django.http.response import HttpResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView 
from django.http import HttpResponse
from blog.models import Post
from .serializers import PostSerializer


def guid(request):
    return HttpResponse("""
    <ul>
        <li>posts list    -> api/posts</li>
        <li>posts details -> api/posts/{id}</li>
    </ul>
    """)


class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailsAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer