from django.shortcuts import render, redirect
from django.contrib import messages
from ..forms.captura_inicial import CapturaTelefonoForm

def iniciar_captura_lead(request):

    if request.method == 'POST':
        form = CapturaTelefonoForm(request.POST)
        
        if form.is_valid():
            numero_limpio = form.cleaned_data['numero_marcado']
            observacion = form.cleaned_data['observacion']
            
            request.session['lead_temporal_telefono'] = numero_limpio
            request.session['lead_temporal_observacion'] = observacion
            
            # (AQUÍ HAREMOS LA CONSULTA A LA BD MÁS ADELANTE PARA SABER SI ES DUPLICADO)
            # Por ahora, solo le diremos al sistema: "Todo salió bien, llévalo al Paso 2"
            
            # Mostramos un mensajito verde de éxito temporalmente para saber que funciona
            messages.success(request, f"Teléfono {numero_limpio} capturado en memoria.")
            
            # Redirigimos al mismo lugar por ahora, luego cambiaremos esto al Formulario 2
            return redirect('captura_inicial') 
            
    # ESCENARIO 2: El asesor apenas entró a la página y necesita ver el formato vacío
    else:
        form = CapturaTelefonoForm() # Creamos un papel en blanco

    # EL DESENLACE: El Gerente (Vista) le pasa el formato (Form) al Diseñador (HTML)
    contexto = {
        'form': form,
        'titulo_pagina': 'Paso 1: Validación de Número'
    }
    return render(request, 'leads/captura_inicial.html', contexto)