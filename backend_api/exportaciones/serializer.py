from rest_framework import serializers
from .models import Exportacion, Pais
from productos.serializer import ProductoSerializer
from geo.serializer import PaisSerializer

class ExportacionesSerializer(serializers.ModelSerializer):
    # destino = PaisSerializer(read_only=True)
    destino = serializers.SerializerMethodField()
    producto = ProductoSerializer(read_only=True)

    class Meta:
        model = Exportacion
        fields = ['id', 'destino', 'producto', 'fob_dolar', 'peso_neto', 'año']
    
    def get_destino(self, obj):
        coordenadas = obj.destino.coordenadas
        if coordenadas:
            return {
                'nombre': obj.destino.nombre,
                'coordenadas': [coordenadas.x,coordenadas.y]  # Formato [lon, lat]
            }
        else:
            return {
                'nombre': obj.destino.nombre,
                'coordenadas': None
            }