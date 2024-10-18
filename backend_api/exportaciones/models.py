from django.db import models
from productos .models import Producto
from geo .models import Pais

class Exportacion(models.Model):
  destino = models.ForeignKey(Pais, on_delete=models.CASCADE)
  producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
  fob_dolar = models.FloatField()
  peso_neto = models.FloatField()
  año = models.IntegerField(verbose_name="Año")
  def __str__(self):
    return f"Exportacion a {self.destino.nombre}"

  class Meta:
        verbose_name = 'Exportación'
        verbose_name_plural = 'Exportaciones'

# Create your models here.
