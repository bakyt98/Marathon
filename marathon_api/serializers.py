from marathon_api.models import Event, Photo
from django.contrib.auth.models import User
from rest_framework import serializers


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name')


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ('id', 'urlOriginal', 'urlCompressed', 'watermark', 'event', 'created_by')
