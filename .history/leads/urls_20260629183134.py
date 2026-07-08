# leads/urls.py
from django.urls import path
from .views.persona import crear_persona

urlpatterns = [
    path('crear-persona/', crear_persona, name='crear_persona'),
]