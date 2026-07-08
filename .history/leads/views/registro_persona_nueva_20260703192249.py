from django.shortcuts import render, redirect
from ..forms.registro_persona_nueva import PersonaNuevaForm

def registro_persona_nueva(request):
    # Recuperamos el teléfono de la "mochila" (Sesión)
    telefono_capturado = request.session.get('lead_temporal_telefono', '')

    if request.method == 'POST':
        form = PersonaNuevaForm(request.POST)
        if form.is_valid():
            # 1. Guardamos la persona en la BD
            nueva_persona = form.save() 
            
            # 2. Ahora que tenemos la persona, CREAMOS EL LEAD (el "doliente")
            # (Aquí importaremos tu modelo Leads y haremos el .create()
            # asignando el id_persona, el teléfono, estado='NUEVO')
            
            return redirect('alguna_ruta_siguiente') 
    else:
        # Iniciamos el formulario y PRE-LLENAMOS el teléfono bloqueado
        form = PersonaNuevaForm(initial={'telefono_referencia': telefono_capturado})

    return render(request, 'leads/registro_persona_nueva.html', {'form': form})