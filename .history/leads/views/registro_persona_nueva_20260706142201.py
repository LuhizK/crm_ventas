from django.shortcuts import render, redirect
from django.db import transaction
from django.http import HttpResponse
from datetime import datetime
from ..forms.registro_persona_nueva import PersonaNuevaForm
from ..models import Leads, Observaciones, Trabajador, Telefonos # Traemos al Trabajador real

def registro_persona_nueva(request):
    # 1. Validación de flujo
    telefono = request.session.get('lead_temporal_telefono')
    if not telefono:
        return redirect('captura_inicial')

    if request.method == 'POST':
        form = PersonaNuevaForm(request.POST)
        
        if form.is_valid():
            try:
                with transaction.atomic():
                    # A. Guardamos la Persona (esto funciona porque es un ModelForm)
                    nueva_persona = form.save()
                    
                    # B. Buscamos el primer trabajador de tu base de datos
                    # (Más adelante lo cambiaremos por el trabajador logueado)
                    trabajador_asignado = Trabajador.objects.first()
                    if not trabajador_asignado:
                        raise Exception("CRÍTICO: No hay registros en la tabla 'trabajador'. Crea uno en pgAdmin primero.")

                    # C. Creamos Lead (El Doliente)
                    nuevo_lead = Leads.objects.create(
                        id_persona=nueva_persona,
                        id_trabajador=trabajador_asignado, 
                        telefono_marcado=telefono,
                        estado_lead='NUEVO'
                    )
                    
                    Telefonos.objects.create(
                        numero_telefono=telefono,
                        tipo_telefono='PRINCIPAL',
                        id_persona=nueva_persona
                    )
                    
                    telefono_sec = form.cleaned_data.get('telefono_secundario')
                    if telefono_sec:
                        Telefonos.objects.create(
                            numero_telefono=telefono_sec.strip(),
                            tipo_telefono='SECUNDARIO',
                            id_persona=nueva_persona
                        )
                    
                    # D. Guardamos la observación inicial en la tabla correspondiente
                    Observaciones.objects.create(
                        id_lead=nuevo_lead,
                        id_trabajador=trabajador_asignado,
                        observacion=form.cleaned_data['observacion_referencia'],
                        fecha_registro=datetime.now() 
                    )
                    
                    # E. Limpieza de memoria RAM
                    del request.session['lead_temporal_telefono']
                    del request.session['lead_temporal_observacion']
                    
                    # REDIRECCIÓN FINAL (Éxito)
                    return redirect('captura_inicial') 
                    
            except Exception as e:
                # SI LA BASE DE DATOS RECHAZA EL REGISTRO, VERÁS ESTO EN PANTALLA
                return HttpResponse(f"<h1>Error en la Base de Datos</h1><p>{str(e)}</p>")
                
        else:
            # SI EL FORMULARIO LE FALTA UN CAMPO, VERÁS ESTO EN PANTALLA
            return HttpResponse(f"<h1>Error en el Formulario</h1><p>{form.errors}</p>")

    else:
        # Pre-llenamos los campos bloqueados para el método GET
        form = PersonaNuevaForm(initial={
            'telefono_referencia': telefono,
            'observacion_referencia': request.session.get('lead_temporal_observacion', '')
        })

    return render(request, 'leads/registro_persona_nueva.html', {'form': form})