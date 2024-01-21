from rest_framework import serializers
from .models import Threads


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Threads
        fields = "__all__"
