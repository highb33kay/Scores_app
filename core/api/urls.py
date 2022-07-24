from django.contrib import admin
from django.urls import path, include
from .views import GameView

urlpatterns = [
    path("api/", GameView.as_view()),
]
