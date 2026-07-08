from django.shortcuts import render, redirect, get_object_or_404
from ..models import Ciudad
from ..forms.ciudades import CiudadForm

# --- 1. VISTA DE LECTURA (LISTA) ---
def listar_ciudades(request):
    # .all() trae todos los registros, y los ordenamos alfabéticamente
    ciudades = Ciudad.objects.all().order_by('ciudad')
    return render(request, 'leads/listar_ciudades.html', {'ciudades': ciudades})

# --- 2. VISTA HÍBRIDA (CREAR / EDITAR) ---
def crear_editar_ciudad(request, id_ciudad=None):
    # Si la URL trae un ID, buscamos la ciudad en la base de datos. 
    # Si no trae ID, definimos la variable como None (es un registro nuevo).
    ciudad_instancia = get_object_or_404(Ciudad, id_ciudad=id_ciudad) if id_ciudad else None

    if request.method == 'POST':
        # El parámetro 'instance' es la magia:
        # Si instance=None, Django hace un INSERT (crear).
        # Si instance tiene datos, Django hace un UPDATE (editar).
        form = CiudadForm(request.POST, instance=ciudad_instancia)
        
        if form.is_valid():
            form.save() # Guarda directo en la base de datos sin necesidad de hacer .create()
            return redirect('listar_ciudades')
    else:
        # GET: Cargar el formulario (vacío o pre-llenado si estamos editando)
        form = CiudadForm(instance=ciudad_instancia)

    # Le pasamos una variable 'es_edicion' al HTML para cambiar el título (Crear vs Editar)
    return render(request, 'leads/form_ciudad.html', {
        'form': form,
        'es_edicion': True if id_ciudad else False
    })