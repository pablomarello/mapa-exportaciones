from django.db import models

class Pregunta (models.Model):
    question = models.CharField(max_length=255,verbose_name='Pregunta')
    correct_answer = models.CharField(max_length=255,verbose_name='Respuesta Correcta')
    publicada = models.BooleanField(default=True)

    def __str__(self):
        return self.question
    
    class Meta:
        verbose_name = 'Pregunta'
        verbose_name_plural = 'Preguntas'

class RespuestaIncorrecta(models.Model):
    question_inc = models.ForeignKey(Pregunta, related_name='incorrect_answers',verbose_name='Pregunta', on_delete=models.CASCADE)
    answer_incorrect = models.CharField(max_length=255,verbose_name='Respuesta Incorrecta')

    def __str__(self):
        return self.answer_incorrect
    
    class Meta:
        verbose_name = 'Respuesta Incorrecta'
        verbose_name_plural = 'Respuestas Incorrectas'

# Create your models here.
