from django.shortcuts import render
from rest_framework import generics
from .serializers import RoomSerializer
from .models import Room

# RoomVIew inherit from generics
"""here we set a view that will rturn us all of the different room object"""
class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()   # this allow us not only view all the rooms but also create
    serializer_class = RoomSerializer
