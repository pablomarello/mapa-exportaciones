from django.db import models
from django.contrib.gis.db import models as gis_models

class Continente(models.Model):
  nombre = models.CharField(max_length=100)
  def __str__(self):
        return self.nombre
  class Meta:
        verbose_name = 'Continente'
        verbose_name_plural = 'Continentes'
  
class Pais(models.Model):
  nombre = models.CharField(max_length=100, unique=True)
  continente = models.ForeignKey(Continente, on_delete=models.CASCADE, related_name='paises')
  coordenadas = gis_models.PointField(geography=True, blank=True, null=True)  
  def __str__(self):
        return self.nombre
  class Meta:
        verbose_name = 'Pais '
        verbose_name_plural = 'Paises'
  
# Create your models here.
