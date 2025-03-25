from rest_framework import serializers

from clients.models import MeetingModel

class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeetingModel
        fields = '__all__'
