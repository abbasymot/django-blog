from django.urls import path
from .views import PostListAPIView, PostDetailsAPIView, guid

urlpatterns = [
    path('', guid, name='guid_api'),
    path('posts/', PostListAPIView.as_view(), name='posts_api'),
    path('posts/<int:pk>/', PostDetailsAPIView.as_view(), name='posts_api'),
]