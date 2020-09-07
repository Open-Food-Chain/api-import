from rest_framework import viewsets
from .models import Batch, Integrity
from .serializers import BatchSerializer, IntegritySerializer


class IntegrityView(viewsets.ModelViewSet):
    queryset = Integrity.objects.all()
    serializer_class = IntegritySerializer


class BatchView(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer
