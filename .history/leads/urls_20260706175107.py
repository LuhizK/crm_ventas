from django.urls import path
from .views.captura_inicial import iniciar_captura_lead
from .views.registro_persona_nueva import registro_persona_nueva
from .views.registro_plataformas import registro_plataformas

urlpatterns = [
    # Cuando visiten /leads/nuevo/, se ejecuta iniciar_captura_lead
    path('nuevo/', iniciar_captura_lead, name='captura_inicial'),
    path('registro-persona/', registro_persona_nueva, name='registro_persona_nueva'),
]