from rest_framework import serializers
from .models import Batch, Integrity


class IntegritySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Integrity
        fields = ('id', 'name')


class BatchSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Batch
        fields = ('id', 'name')
