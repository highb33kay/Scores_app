from django.shortcuts import render
from rest_framework import generics
from .models import Game
from .serializers import GameSerializer
# Create your views here.


class GameView(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
