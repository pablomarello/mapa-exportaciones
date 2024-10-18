from django.utils.html import format_html
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Producto

class ProductoResource(resources.ModelResource):
  
  class Meta:
    model = Producto
    fields = ('nombre','rubro')
    exclude = ('id',)
    import_id_fields = ['nombre', 'rubro']

  def before_import_row(self, row, **kwargs):
        
        if 'id' in row:
            del row['id']

class ProductoAdmin(ImportExportModelAdmin):
  resource_class = ProductoResource
  list_display = ('id','nombre','rubro','imagen_thumbnail')

  def imagen_thumbnail(self, obj):
        if obj.imagen:
            return format_html('<img src="{}" width="100" height="100" />', obj.imagen.url)
        return 'Sin imagen'
  imagen_thumbnail.short_description = 'Imagen'
    
  ordering = ('nombre','id','rubro',)
  search_fields = ('id','nombre',)
  list_display_links = ('nombre',)
  list_filter = ('rubro',)

admin.site.register(Producto, ProductoAdmin)
# Register your models here.
