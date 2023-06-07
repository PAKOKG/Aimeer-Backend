from rest_framework import serializers
from .models import Feedback, ConnectWithUs

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'

class ConnectWithUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConnectWithUs
        fields = '__all__'