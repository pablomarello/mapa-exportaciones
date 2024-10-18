from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializer import ExportacionesSerializer
from .models import Exportacion, Pais
from exportaciones.serializer import  ExportacionesSerializer
from .serializer import PaisSerializer, ProductoSerializer



class ExportacionView(viewsets.ModelViewSet):
    queryset = Exportacion.objects.all()
    serializer_class = ExportacionesSerializer





# Create your views here.
