from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import ProfileUpdateView, profile


urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),


    path('<slug:slug>/', profile, name='profile'),
    path('<slug:slug>/update/', ProfileUpdateView.as_view(), name='update_profile'),

]