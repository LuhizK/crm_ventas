from django.urls import path
from .views.captura_inicial import iniciar_captura_lead
from .views.registro_persona_nueva import registro_persona_nueva
from .views.registro_plataformas import registro_plataformas
from .views.crear_acuerdo import crear_acuerdo_pago

urlpatterns = [
    path('', panel_control, name='panel_control'),
    path('nuevo/', iniciar_captura_lead, name='captura_inicial'),
    path('registro-persona/', registro_persona_nueva, name='registro_persona_nueva'),
    path('plataformas/<int:id_lead>/', registro_plataformas, name='registro_plataformas'),
    path('crear-acuerdo/<int:id_lead>/', crear_acuerdo_pago, name='crear_acuerdo_pago'),
]