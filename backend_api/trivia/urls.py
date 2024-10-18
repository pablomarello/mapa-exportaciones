from django.urls import path, include
from rest_framework import routers
from trivia import views

router = routers.DefaultRouter()
router.register(r'pregunta', views.PreguntaView, 'pregunta')
router.register(r'respuestaincorrecta', views.RespuestaIncorrectaView, 'respuestaincorrecta')

urlpatterns = [
    path('tri/', include(router.urls)),
]