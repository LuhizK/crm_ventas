# leads/views/persona.py
from django.shortcuts import render, redirect
from ..forms.persona import PersonaForm

def crear_persona(request):
    # Si la petición es POST (el usuario le dio al botón de guardar)
    if request.method == 'POST':
        form = PersonaForm(request.POST) # Cargamos los datos enviados
        if form.is_valid(): # ¿Están todos los datos correctos?
            form.save() # ¡Lo guardamos en la base de datos!
            return redirect('lista_personas') # Redirigimos a una página de éxito (crearemos esta ruta luego)
    
    # Si la petición es GET (el usuario apenas entró a la página)
    else:
        form = PersonaForm() # Le damos un formulario vacío
    
    # Renderizamos la página enviando el formulario al HTML
    return render(request, 'leads/crear_persona.html', {'form': form})