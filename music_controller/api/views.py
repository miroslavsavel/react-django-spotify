from django.shortcuts import render
from rest_framework import generics, status
from .serializers import RoomSerializer, CreateRoomSerializer
from .models import Room

from rest_framework.views import APIView
from rest_framework.response import Response

# RoomVIew inherit from generics
"""here we set a view that will rturn us all of the different room object"""
class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()   # this allow us not only view all the rooms but also create
    serializer_class = RoomSerializer

class CreateRoomView(APIView):
    serializer_class = CreateRoomSerializer

    def post(self, request, format=None):
        #accesstto session id, we will check if session key exists
        if not self.request.session.exists(self.request.session.session_key):
            #if doesnt exists
            self.request.session.create()

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            guest_can_pause = serializer.data.get('guest_can_pause')
            votes_to_skip = serializer.data.get('votes_to_skip')
            host = self.request.session.session_key
            queryset = Room.objects.filter(host=host)
            if queryset.exists():
                room = queryset[0]
                room.guest_can_pause = guest_can_pause
                room.votes_to_skip = votes_to_skip
                room.save(update_fields=['guest_can_pause', 'votes_to_skip'])
                return Response(RoomSerializer(room).data, status=status.HTTP_200_OK)
            else:
                room = Room(host=host, guest_can_pause=guest_can_pause, votes_to_skip=votes_to_skip)
                room.save() #this create the room
                return Response(RoomSerializer(room).data,status=status.HTTP_201_CREATED) #we need to serialize the room object we have just created, this create json format
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)