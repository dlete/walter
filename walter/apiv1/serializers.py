# Core Django imports
from django.contrib.auth.models import User, Group

# Third-party app imports
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        #fields = ('url', 'username', 'email', 'groups')
        fields = ('username', 'email')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')
