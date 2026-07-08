from django.urls import path
from .views.captura_inicial import iniciar_captura_lead

urlpatterns = [
    # Cuando visiten /leads/nuevo/, se ejecuta iniciar_captura_lead
    path('nuevo/', iniciar_captura_lead, name='captura_inicial'),
]