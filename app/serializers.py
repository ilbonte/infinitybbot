from django.contrib.auth.models import User, Group
from rest_framework import serializers

from app.models import Pong


class PongSerializer(serializers.Serializer):
    ping = serializers.CharField(allow_blank=True,
                                 default="ping",
                                 max_length=10,
                                 help_text="please input 'ping'")


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']