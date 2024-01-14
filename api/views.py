from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *

# Create your views here.


class ThreadAPIView(viewsets.ModelViewSet):
    queryset = Threads.objects.all()
    serializer_class = ThreadSerializer

