from django.urls import path
from .views import register, profile , home
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home, name='blog_home'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name = 'blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),

]