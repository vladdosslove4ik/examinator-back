from rest_framework import serializers
from base.models import *

class ModeratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moderator
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class BusinessUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessUser
        fields = "__all__"
