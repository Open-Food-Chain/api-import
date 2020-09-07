from rest_framework import serializers
from .models import Batch, Integrity


class IntegritySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)

    class Meta:
        model = Integrity
        fields = ('id', 'integrity_address', 'integrity_pre_tx', 'integrity_post_tx', 'batch')


class BatchSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    integrity_details = IntegritySerializer(read_only=True)

    class Meta:
        model = Batch
        fields = ('id', 'anfp', 'dfp', 'bnfp', 'pds', 'pde', 'jds', 'jde', 'bbd', 'pc', 'pl', 'rmn', 'pon', 'pop', 'raw_json', 'integrity_details')
