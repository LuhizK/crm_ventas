from django.shortcuts import render, redirect, get_object_or_404
from ..models import Sede
from ..forms.sedes import SedeForm

def listar_sedes(request):
    sedes = Sede.objects.all()
    return render(request, 'leads/listar_sedes.html', {'sedes': sedes})

def crear_editar_sede(request, id_sede=None):
    # Si id_sede existe, buscamos la sede, si no, es None (creación)
    sede_instancia = get_object_or_404(Sede, id_sede=id_sede) if id_sede else None
    
    if request.method == 'POST':
        form = SedeForm(request.POST, instance=sede_instancia)
        if form.is_valid():
            form.save()
            return redirect('listar_sedes')
    else:
        form = SedeForm(instance=sede_instancia)
        
    return render(request, 'leads/form_sede.html', {
        'form': form, 
        'es_edicion': id_sede is not None
    })