from django.urls import path

from posts import views

urlpatterns = [
    path(r'posts/', views.CreatePostView.as_view(), name='create-post'),
]
