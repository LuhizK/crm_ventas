from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from ..models import Leads, Persona, Observaciones
from ..forms.editar_lead import EditarLeadForm, EditarEstadoLeadForm

def editar_lead(request, id_lead):
    lead = get_object_or_404(Leads, id_lead=id_lead)
    persona = lead.id_persona
    historial_obs = Observaciones.objects.filter(id_lead=lead).order_by('-fecha_registro')

    if request.method == 'POST':
        form_p = EditarLeadForm(request.POST, instance=persona)
        form_l = EditarEstadoLeadForm(request.POST, instance=lead)

        nueva_obs_texto = request.POST.get('nueva_observacion')
        
        if form_p.is_valid() and form_l.is_valid():
            with transaction.atomic():
                form_p.save()
                form_l.save()
                if nueva_obs_texto:
                    Observaciones.objects.create(
                        id_lead=lead,
                        id_trabajador=None, # O asigna el trabajador logueado
                        observacion=nueva_obs_texto,
                        fecha_registro=lead.fecha_creacion # Ajustar según tu lógica
                    )
            return redirect('editar_lead', id_lead=lead.id_lead)

    else:
        form_p = EditarLeadForm(instance=persona)
        form_l = EditarEstadoLeadForm(instance=lead)

    return render(request, 'leads/editar_lead.html', {
        'form_p': form_p,
        'form_l': form_l,
        'lead': lead,
        'historial_obs': historial_obs
    })