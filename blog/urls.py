from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('create/',views.create, name='blog-about'),
    path('store/', views.store, name='blog-post-store'),
    path('<int:post_id>/show', views.show, name='blog-post-detail'),
    path('<int:post_id>/edit', views.edit, name='blog-post-edit'),
]