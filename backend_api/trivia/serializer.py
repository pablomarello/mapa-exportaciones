from rest_framework import serializers
from .models import Pregunta, RespuestaIncorrecta

class PreguntaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pregunta
    fields = '__all__'

class RespuestaIncorrectaSerializer(serializers.ModelSerializer):
  class Meta:
    model = RespuestaIncorrecta
    fields = '__all__'