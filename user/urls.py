from django.urls import path

from .views import (
    user,
    user_detail
)

urlpatterns = [
    path('users/', user),
    path('users/<int:pk>/', user_detail)
]