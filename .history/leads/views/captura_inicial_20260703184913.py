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
            
            # 1. Guardamos en la memoria RAM temporal (Sesión)
            request.session['lead_temporal_telefono'] = numero_limpio
            request.session['lead_temporal_observacion'] = observacion
            
            
            messages.success(request, f"Teléfono {numero_limpio} capturado en memoria.")
            
            return redirect('captura_inicial') 

    else:
        form = CapturaTelefonoForm() # Creamos un papel en blanco

    contexto = {
        'form': form,
        'titulo_pagina': 'Paso 1: Validación de Número'
    }
    return render(request, 'leads/captura_inicial.html', contexto)