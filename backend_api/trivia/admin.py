from django.contrib import admin
from trivia.models import Pregunta, RespuestaIncorrecta
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class PreguntaAdmin(admin.ModelAdmin):
  list_display = (
    'id',
    'question',
    'correct_answer',
    'publicada'
  )
  list_display_links = ('question',)
  list_editable = ('publicada',)

class RespuestaIncorrectaAdmin(admin.ModelAdmin):
  list_display = ('id', 'question_inc', 'answer_incorrect')

admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(RespuestaIncorrecta, RespuestaIncorrectaAdmin)


# Register your models here.
