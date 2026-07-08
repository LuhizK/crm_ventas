from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib.auth.models import User
from ..forms.registro_persona_nueva import PersonaNuevaForm
from ..models import Leads

def registro_persona_nueva(request):
    # SEGURIDAD: Validación de flujo (Candado de seguridad)
    telefono = request.session.get('lead_temporal_telefono')
    if not telefono:
        return redirect('captura_inicial')

    if request.method == 'POST':
        form = PersonaNuevaForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    # 1. Guardamos la Persona
                    nueva_persona = form.save()
                    
                    # 2. Buscamos un trabajador existente para cumplir con la restricción de la BD
                    from ..models import Trabajador
                    trabajador_asignado = Trabajador.objects.first()
                    
                    if not trabajador_asignado:
                        raise Exception("No hay trabajadores registrados en la base de datos para asignar al Lead.")

                    # 3. Crear el Lead cumpliendo con todas las llaves foráneas obligatorias
                    Leads.objects.create(
                        id_persona=nueva_persona,
                        id_trabajador=trabajador_asignado, # Requerido por tu modelo
                        telefono_marcado=telefono,          # Campo que acordamos usar
                        estado_lead='NUEVO'                 # Tu campo de estado
                    )
                    
                    # Limpiamos la sesión
                    del request.session['lead_temporal_telefono']
                    del request.session['lead_temporal_observacion']
                    
                    # TODO: Cambiar por la vista de gestión o detalle del Lead creado
                    return redirect('captura_inicial') 
            except Exception as e:
                print(f"Error crítico en el proceso atómico: {e}")
                # Aquí deberíamos notificar al asesor que algo salió mal
                
    else:
        form = PersonaNuevaForm(initial={
            'telefono_referencia': telefono,
            'observacion_referencia': request.session.get('lead_temporal_observacion', '')
        })

    return render(request, 'leads/registro_persona_nueva.html', {'form': form})