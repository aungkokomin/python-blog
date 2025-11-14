from django.urls import path
from .views import post_view, author_view, auth_view

urlpatterns = [
    path('login/', auth_view.login_view, name='login'),
    path('', post_view.home, name='blog-home'),
    path('create/',post_view.create, name='blog-about'),
    path('store/', post_view.store, name='blog-post-store'),
    path('<int:post_id>/show', post_view.show, name='blog-post-detail'),
    path('<int:post_id>/edit', post_view.edit, name='blog-post-edit'),
]