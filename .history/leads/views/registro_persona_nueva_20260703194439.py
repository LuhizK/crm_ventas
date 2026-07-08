from django.shortcuts import render, redirect
from ..forms.registro_persona_nueva import PersonaNuevaForm

def registro_persona_nueva(request):
    # Recuperamos el teléfono de la sesión
    telefono = request.session.get('lead_temporal_telefono', '')

    if request.method == 'POST':
        form = PersonaNuevaForm(request.POST)
        if form.is_valid():
            # Aquí vendrá la lógica del transaction.atomic
            return redirect('alguna_ruta_final') 
    else:
        # Pre-llenamos el formulario con el teléfono bloqueado y la observación
        form = PersonaNuevaForm(initial={
            'telefono_referencia': telefono,
            'observacion_referencia': request.session.get('lead_temporal_observacion', '')
        })

    return render(request, 'leads/registro_persona_nueva.html', {'form': form})