from django.urls import path
from .views import(
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views

urlpatterns = [
    path('', views.home, name='blog_home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('posts/', PostListView.as_view(), name='list_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('create_post/', PostCreateView.as_view(), name='post_create' ),
    path('update_post/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('delete_post/<int:pk>/', PostDeleteView.as_view(), name='post_confirm_delete'),
]