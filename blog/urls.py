from django.urls import path
from .views import PostDeleteView, PostDetailView, PostListView, SearchListView, post_create, post_update


urlpatterns = [
    path('', PostListView.as_view(), name='posts'), # all of the posts
    path('post/<slug:slug>', PostDetailView.as_view(), name='post'), # singe post details
    path('post/<slug:slug>/update/', post_update, name='update'), # update a post
    path('post/<slug:slug>/delete/', PostDeleteView.as_view(), name='delete'), # delete a post
    # path('post/create/', PostCreateView.as_view(), name='create'), # delete a post
    path('post/create/', post_create, name='create'), # delete a post

    path('search/', SearchListView.as_view(), name='search'),

]