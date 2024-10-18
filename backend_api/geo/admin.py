from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Continente, Pais
from leaflet.admin import LeafletGeoAdmin

class PaisResource(resources.ModelResource):
  fields = (
    'id',
    'nombre',
    'continente',
    'coordenadas',

  )
  class Meta:
    model = Pais

class ContinenteResource(resources.ModelResource):
  fields = (
    'nombre',
  )
  class Meta:
    model = Continente

class ContinenteAdmin(ImportExportModelAdmin):
  list_display = ('id','nombre')

class PaisAdmin(ImportExportModelAdmin,LeafletGeoAdmin):
  resource_class = PaisResource
  list_display = ('id','nombre','continente','coordenadas')
  ordering = ('nombre',)
  search_fields = ('id','nombre',)
  list_display_links = ('nombre',)
  list_filter = ('continente',)

admin.site.register(Continente, ContinenteAdmin)
admin.site.register(Pais, PaisAdmin)

# Register your models here.
