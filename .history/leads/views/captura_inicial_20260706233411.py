from django.shortcuts import render, redirect
from django.contrib import messages
from ..forms.captura_inicial import CapturaTelefonoForm
from ..models import Telefonos # IMPORTANTE: Traemos el mapa de la tabla Telefonos

def iniciar_captura_lead(request):

    if request.method == 'POST':
        form = CapturaTelefonoForm(request.POST)
        
        if form.is_valid():
            numero_limpio = form.cleaned_data['numero_marcado']
            observacion = form.cleaned_data['observacion']

            request.session['lead_temporal_telefono'] = numero_limpio
            request.session['lead_temporal_observacion'] = observacion
            
            telefono_existe = Telefonos.objects.filter(numero_telefono=numero_limpio).first()
            

            if telefono_existe:
                # ESCENARIO A: El número YA existe en la BD
                messages.warning(request, f"¡Atención! El número {numero_limpio} ya está registrado en el sistema. (Opciones de duplicado en construcción...)")
                return redirect('captura_inicial')
            else:
                # ESCENARIO B: El número NO existe. Es un Lead 100% nuevo.
                messages.success(request, f"Número {numero_limpio} verificado. Libre para registro.")

                return redirect('registro_persona_nueva')

    else:
        form = CapturaTelefonoForm() # Creamos un papel en blanco

    contexto = {
        'form': form,
        'titulo_pagina': 'Paso 1: Validación de Número'
    }
    return render(request, 'leads/captura_inicial.html', contexto)