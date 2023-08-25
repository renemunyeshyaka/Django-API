from rest_framework import serializers
from .models import Fridge
class FridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fridge
        fields = ['id', 'name', 'description']