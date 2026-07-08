from django.shortcuts import render, redirect, get_object_or_404
from ..models import Trabajador, Cargo
from ..forms.trabajadores import TrabajadorForm

def asegurar_cargos_basicos():
    # INYECCIÓN AUTOMÁTICA: Esto es momentáneo, posterior realizaremos la carga por web.
    cargos_requeridos = ['Asesor', 'Coach', 'Gerente Sede', 'Calidad', 'Gerente General']
    for nombre in cargos_requeridos:
        Cargo.objects.get_or_create(
            nombre_cargo=nombre, 
            defaults={'descripcion_cargo': f'Rol operativo de {nombre}'}
        )

def listar_trabajadores(request):
    asegurar_cargos_basicos() # Verificación silenciosa antes de listar
    trabajadores = Trabajador.objects.all().select_related('id_persona', 'id_sede', 'id_cargo')
    return render(request, 'leads/listar_trabajadores.html', {'trabajadores': trabajadores})

def crear_editar_trabajador(request, id_trabajador=None):
    asegurar_cargos_basicos() # Verificación silenciosa antes de cargar el formulario
    
    trabajador_instancia = get_object_or_404(Trabajador, id_trabajador=id_trabajador) if id_trabajador else None

    if request.method == 'POST':
        form = TrabajadorForm(request.POST, instance=trabajador_instancia)
        if form.is_valid():
            form.save()
            return redirect('listar_trabajadores')
    else:
        form = TrabajadorForm(instance=trabajador_instancia)

    return render(request, 'leads/form_trabajador.html', {
        'form': form,
        'es_edicion': True if id_trabajador else False
    })