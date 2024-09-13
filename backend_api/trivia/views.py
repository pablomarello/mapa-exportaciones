from django.shortcuts import render
from rest_framework import viewsets
from .serializer import PreguntaSerializer, RespuestaIncorrectaSerializer
from .models import Pregunta, RespuestaIncorrecta

class PreguntaView(viewsets.ModelViewSet):
  serializer_class = PreguntaSerializer
  queryset = Pregunta.objects.filter(publicada=True)  # envia al front solo las preguntas publicadas
  """ queryset = Pregunta.objects.all() #envia al front todas las preguntas """

class RespuestaIncorrectaView(viewsets.ModelViewSet):
  serializer_class = RespuestaIncorrectaSerializer
  queryset = RespuestaIncorrecta.objects.all()
  

# Create your views here.
