from django.urls import path
from .views import register, profile , PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, CommentUpdateView, CommentDeleteView, CommentCreateView, PostSearchView,PostByTagListView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', PostListView.as_view(),  name='blog_home'),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name = 'blog/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', profile, name='profile'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name = 'post_new'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post_delete'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name = 'comment_create'),
    path('post/<int:post_pk>/comment/<int:pk>/update/', CommentUpdateView.as_view(), name = 'comment_update'),
    path('post/<int:post_pk>/comment/<int:pk>/delete/', CommentDeleteView.as_view(), name = 'comment_delete'),
    path('post/search/', PostSearchView.as_view(), name = 'post_search'),
    path('tags/<slug:tag_slug>/', PostByTagListView.as_view(), name = 'posts_by_tag'),

]