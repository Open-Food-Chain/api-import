from django.shortcuts import render
from rest_framework import viewsets
from .models import Bottler
from .serializers import BottlerSerializer

class BottlerView(viewsets.ModelViewSet):
  queryset = Bottler.objects.all()
  serializer_class = BottlerSerializer
