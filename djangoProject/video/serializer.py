from rest_framework import serializers
from . models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Video
        field='__all__'

