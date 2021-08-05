from django.urls import path

from . import views

urlpatterns = [
    path('lista/', views.index),
    path('<slug:video_id>', views.view_video)
]