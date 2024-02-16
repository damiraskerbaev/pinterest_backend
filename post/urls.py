from django.urls import path

from .views import (
    post,
    posts_detail
)

urlpatterns = [
    path('', post),
    path('posts/<int:pk>/', posts_detail)
]