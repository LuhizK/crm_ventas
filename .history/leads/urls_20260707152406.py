from django.urls import path
from .views.panel_control import panel_control
from .views.captura_inicial import iniciar_captura_lead
from .views.registro_persona_nueva import registro_persona_nueva
from .views.registro_plataformas import registro_plataformas
from .views.crear_acuerdo import crear_acuerdo_pago
from .views.ciudades import listar_ciudades, crear_editar_ciudad
from .views.sedes import listar_sedes, crear_editar_sede
from .views.trabajadores import listar_trabajadores, crear_editar_trabajador
from .views.leads import listar_leads
from .views.editar_lead import editar_lead

urlpatterns = [
    path('', panel_control, name='panel_control'),
    path('nuevo/', iniciar_captura_lead, name='captura_inicial'),
    path('registro-persona/', registro_persona_nueva, name='registro_persona_nueva'),
    path('plataformas/<int:id_lead>/', registro_plataformas, name='registro_plataformas'),
    path('crear-acuerdo/<int:id_lead>/', crear_acuerdo_pago, name='crear_acuerdo_pago'),
    path('ciudades/', listar_ciudades, name='listar_ciudades'),
    path('ciudades/nueva/', crear_editar_ciudad, name='crear_ciudad'),
    path('ciudades/editar/<int:id_ciudad>/', crear_editar_ciudad, name='editar_ciudad'),
    path('sedes/', listar_sedes, name='listar_sedes'),
    path('sedes/nueva/', crear_editar_sede, name='crear_sede'),
    path('sedes/editar/<int:id_sede>/', crear_editar_sede, name='editar_sede'),
    path('trabajadores/', listar_trabajadores, name='listar_trabajadores'),
    path('trabajadores/nueva/', crear_editar_trabajador, name='crear_trabajador'),
    path('trabajadores/editar/<int:id_trabajador>/', crear_editar_trabajador, name='editar_trabajador'),
    path('leads-historial/', listar_leads, name='listar_leads'),
]