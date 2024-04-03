from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, PostLikeView, CommentCreateView


urlpatterns = [
    # path('', views.blog_home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    # path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/like/<int:pk>/', PostLikeView, name='post-like'),
    path('post/<int:pk>/comment/', CommentCreateView.as_view(), name='comment-create')
]