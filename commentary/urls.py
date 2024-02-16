from django.urls import path

from .views import (
    commentary,
    commentary_detail
)

urlpatterns = [
    path('commentary/', commentary),
    path('commentary/<int:pk>/', commentary_detail)
]