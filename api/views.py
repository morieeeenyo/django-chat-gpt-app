from django.shortcuts import render
from rest_framework import viewsets
from .models import Threads
from .serializers import ThreadSerializer

# Create your views here.


class ThreadViewSet(viewsets.ModelViewSet):
    queryset = Threads.objects.all()
    serializer_class = ThreadSerializer
