from rest_framework import serializers
from .models import Room

"""it will take model room and it will translate it into json response"""
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')     #these fields match the model attributes
