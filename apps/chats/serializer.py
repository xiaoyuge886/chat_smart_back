"""
@ Author:   gy
@ Date :    2022/8/8
"""
from rest_framework import serializers
from apps.chats.models import Record


# Serializers define the API representation.
class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ["content"]
