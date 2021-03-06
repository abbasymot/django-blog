from django.urls import path
from .views import post_delete, post_details, PostListView, SearchListView, post_create, post_update


urlpatterns = [
    path('post/<slug:slug>/', post_details, name='post'), # singe post details
    path('', PostListView.as_view(), name='posts'), # all of the posts
    path('category/<slug:slug>/', PostListView.as_view(), name='categoryposts'), # all of the posts
    path('post/<slug:slug>/update/', post_update, name='update'), # update a post
    path('post/<slug:slug>/delete/', post_delete, name='delete'), # delete a post
    path('create/', post_create, name='create'), # create a post

    path('search/', SearchListView.as_view(), name='search'),

]