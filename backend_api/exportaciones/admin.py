from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget
from django.contrib import admin
from .models import Exportacion, Pais, Producto
from django.utils.formats import localize


admin.site.site_header = 'Secretaría de Relaciones Internacionales'
admin.site.index_title = 'Sitio Administrativo - Mapa de Exportaciones'
admin.site.site_title = 'Secretaría de Relaciones Internacionales'

class ExportacionResource(resources.ModelResource):
  destino = fields.Field(attribute='destino', column_name='destino',widget=ForeignKeyWidget(Pais, 'id'))
  producto = fields.Field(attribute='producto', column_name='producto',widget=ForeignKeyWidget(Producto, 'id'))
  
  def dehydrate_anio(self, exportacion):
        print(f'Exportando año: {exportacion.año}')
        return exportacion.año
  
  class Meta:
    model = Exportacion
    fields = ('destino', 'producto', 'fob_dolar', 'peso_neto', 'año')
    exclude = ('id',)
    import_id_fields = ['destino', 'producto', 'fob_dolar', 'peso_neto', 'año']

  def before_import_row(self, row, **kwargs):
        
        if 'id' in row:
            del row['id']
    
  def dehydrate_destino(self, exportacion):
    return exportacion.destino.nombre if exportacion.destino else 'N/A'

  def dehydrate_producto(self, exportacion):
    return exportacion.producto.nombre if exportacion.producto else 'N/A'

class ExportacionAdmin(ImportExportModelAdmin):
  resource_class = ExportacionResource
  list_display = (
    'destino',
    'producto',
    'formatted_fob_dolar',
    'formatted_peso_neto',
    'año'
    
  )

  # Método para formatear el campo fob_dolar
  def formatted_fob_dolar(self, obj):
        return "{:,.2f}".format(obj.fob_dolar).replace(",", "X").replace(".", ",").replace("X", ".")
  formatted_fob_dolar.short_description = 'FOB DOLAR'

  # Método para formatear el campo peso_neto
  def formatted_peso_neto(self, obj):
        return "{:,.2f}".format(obj.peso_neto).replace(",", "X").replace(".", ",").replace("X", ".")
  formatted_peso_neto.short_description = 'Peso Neto (kg)'

  list_display_links = ('destino','producto',)
  search_fields = (
    'destino__nombre',  
    'producto__nombre',  
    'año',  
)
  list_filter = ('año',)
  ordering = ('-fob_dolar',)
  list_per_page = 30
  


admin.site.register(Exportacion, ExportacionAdmin)

