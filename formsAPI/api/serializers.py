from rest_framework import serializers
from base.models import *


class RozwiazanieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rozwiazanie
        fields = "__all__"

class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test
        fields = "__all__"

class PytanieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pytanie
        fields = "__all__"

class OdpowiedzSerializer(serializers.ModelSerializer):
    class Meta:
        model = Odpowiedz
        fields = "__all__"
