from django.urls import path, include
from rest_framework import routers
from exportaciones import views

router = routers.DefaultRouter()
router.register(r'exportaciones', views.ExportacionView, 'exportaciones')

urlpatterns = [
    path('api/', include(router.urls)),
]