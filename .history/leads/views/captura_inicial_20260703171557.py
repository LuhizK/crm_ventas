from django.shortcuts import render, redirect
from django.contrib import messages
from ..forms.captura_inicial import CapturaTelefonoForm
# En el futuro importaremos el modelo Telefono aquí para buscar en la BD
# from ..models import Telefono 

def iniciar_captura_lead(request):
    """
    EL GERENTE: Esta función maneja la pantalla donde el asesor digita el teléfono.
    """
    
    # ESCENARIO 1: El asesor ya llenó el formato y le dio clic a "Guardar/Siguiente"
    if request.method == 'POST':
        # Le pasamos los datos que llegaron de internet a nuestro Formulario (para que los valide)
        form = CapturaTelefonoForm(request.POST)
        
        # ¿El guardia de seguridad (forms.py) dijo que los datos están limpios?
        if form.is_valid():
            # Extraemos los datos ya limpios de letras y espacios
            numero_limpio = form.cleaned_data['numero_marcado']
            observacion = form.cleaned_data['observacion']
            
            # --- MEMORIA A CORTO PLAZO (SESIÓN) ---
            # En lugar de guardar en la Base de Datos todavía, guardamos el número y la nota
            # en la "mochila" temporal del navegador del asesor (request.session).
            # Así, si cierra la ventana, la base de datos no se llena de basura.
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