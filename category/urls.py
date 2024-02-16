from django.urls import path

from .views import (
    category,
    category_detail
)

urlpatterns = [
    path('category', category),
    path('category/<int:pk>/', category_detail)
]