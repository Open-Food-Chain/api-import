from rest_framework import viewsets
from .models import Batch, Integrity
from .serializers import BatchSerializer, IntegritySerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class IntegrityView(viewsets.ModelViewSet):
    queryset = Integrity.objects.all()
    serializer_class = IntegritySerializer


class BatchView(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer


class BatchNullIntegrityView(APIView):

    def get(self, request, format=None):
        batches = Batch.objects.all()
        serializer = BatchSerializer(batches, many=True)
        return Response(serializer.data)
