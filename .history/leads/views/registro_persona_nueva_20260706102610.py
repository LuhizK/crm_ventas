from django.shortcuts import render, redirect
from django.db import transaction
from django.contrib.auth.models import User
from ..forms.registro_persona_nueva import PersonaNuevaForm
from ..models import Leads, Observaciones # Importamos ambos modelos

def registro_persona_nueva(request):
    telefono = request.session.get('lead_temporal_telefono')
    if not telefono:
        return redirect('captura_inicial')

    if request.method == 'POST':
        form = PersonaNuevaForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    # 1. Guardamos Persona
                    nueva_persona = form.save()
                    
                    # 2. Creamos Lead (Doliente)
                    asesor_temporal = User.objects.first() 
                    nuevo_lead = Leads.objects.create(
                        id_persona=nueva_persona,
                        id_trabajador=asesor_temporal.trabajador, # Asegúrate que User tenga relación con Trabajador
                        telefono_marcado=telefono,
                        estado_lead='NUEVO'
                    )
                    
                    # 3. Guardamos la observación inicial en la tabla correspondiente
                    Observaciones.objects.create(
                        id_lead=nuevo_lead,
                        id_trabajador=asesor_temporal.trabajador,
                        observacion=form.cleaned_data['observacion_referencia'],
                        fecha_registro=datetime.now() # Necesitarás 'from datetime import datetime'
                    )
                    
                    # Limpieza
                    del request.session['lead_temporal_telefono']
                    del request.session['lead_temporal_observacion']
                    
                    # REDIRECCIÓN FINAL
                    return redirect('captura_inicial') 
            except Exception as e:
                # Esto imprimirá el error real en tu consola de VS Code
                print(f"DEBUG ERROR: {e}") 
                # Y también te ayudará a ver si el formulario tenía errores de validación
                print(f"FORM ERRORES: {form.errors}")
    else:
        form = PersonaNuevaForm(initial={
            'telefono_referencia': telefono,
            'observacion_referencia': request.session.get('lead_temporal_observacion', '')
        })

    return render(request, 'leads/registro_persona_nueva.html', {'form': form})