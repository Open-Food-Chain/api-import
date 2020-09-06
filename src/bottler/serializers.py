from rest_framework import serializers
from .models import Bottler


class BottlerSerializer(serializers.ModelSerializer):
    uuid = serializers.UUIDField(read_only=True)

    class Meta:
        model = Bottler
        fields = ('uuid', 'anfp', 'dfp', 'bnfp', 'pds', 'pde', 'jds', 'jde', 'bbd', 'pc', 'pl', 'rmn', 'pon', 'pop', )
