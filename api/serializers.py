from rest_framework import serializers
from datacollection.models import Data
# Create your models here.

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['image', 'username']