from rest_framework import serializers
from . import models

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'