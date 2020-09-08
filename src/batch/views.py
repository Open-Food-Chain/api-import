from rest_framework import viewsets
from .models import Batch, Integrity
from .serializers import BatchSerializer, IntegritySerializer
# from rest_framework.views import APIView
# from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.decorators import action
from rest_framework.response import Response


class IntegrityView(viewsets.ModelViewSet):
    queryset = Integrity.objects.all()
    serializer_class = IntegritySerializer


class BatchView(viewsets.ModelViewSet):
    queryset = Batch.objects.all()
    serializer_class = BatchSerializer

    # from https://stackoverflow.com/a/23836288
    # from https://www.django-rest-framework.org/api-guide/viewsets/
    # #marking-extra-actions-for-routing
    @action(detail=False)  # listview
    def require_integrity(self, request, pk=None):
        null_integrity = Batch.objects.filter(
            integrity_details__isnull=True
        )
        serializer = self.get_serializer(null_integrity, many=True)
        return Response(serializer.data)
