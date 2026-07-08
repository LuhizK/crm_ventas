from django.shortcuts import render, redirect
from django.db import transaction
from ..forms.registro_persona_nueva import PersonaNuevaForm

def registro_persona_nueva(request):
    # SEGURIDAD: Validación de flujo (Candado de seguridad)
    # Si no hay teléfono en sesión, el usuario intentó saltarse el Paso 1
    telefono = request.session.get('lead_temporal_telefono')
    if not telefono:
        return redirect('captura_inicial')

    if request.method == 'POST':
        form = PersonaNuevaForm(request.POST)
        if form.is_valid():
            # --- LÓGICA DE ATOMICIDAD ---
            # Guardamos Persona y Lead en un solo bloque seguro
            try:
                with transaction.atomic():
                    # 1. Guardamos la Persona
                    nueva_persona = form.save()
                    
                    # TODO: Capturar asesor desde request.user (cuando se implemente login)
                    # 2. Crear el Lead asociado
                    # Lead.objects.create(
                    #     persona=nueva_persona,
                    #     telefono=telefono,
                    #     observacion=form.cleaned_data['observacion_referencia'],
                    #     asesor=request.user, 
                    #     estado='NUEVO'
                    # )
                    
                    # Limpiamos la sesión al finalizar exitosamente
                    del request.session['lead_temporal_telefono']
                    del request.session['lead_temporal_observacion']
                    
                    return redirect('captura_inicial') # Redirigir a vista de seguimiento
            except Exception as e:
                # Si algo falla, el rollback es automático por transaction.atomic
                print(f"Error crítico al guardar: {e}")
                
    else:
        # Pre-llenamos el formulario
        form = PersonaNuevaForm(initial={
            'telefono_referencia': telefono,
            'observacion_referencia': request.session.get('lead_temporal_observacion', '')
        })

    return render(request, 'leads/registro_persona_nueva.html', {'form': form})