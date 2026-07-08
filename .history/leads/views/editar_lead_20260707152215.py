from django.shortcuts import render, redirect, get_object_or_404
from ..models import Leads, Persona, Observaciones
from ..forms.editar_lead import EditarLeadForm, EditarEstadoLeadForm

def editar_lead(request, id_lead):
    lead = get_object_or_404(Leads, id_lead=id_lead)
    persona = lead.id_persona
    obs = Observaciones.objects.filter(id_lead=lead).first()

    if request.method == 'POST':
        form_p = EditarLeadForm(request.POST, instance=persona)
        form_l = EditarEstadoLeadForm(request.POST, instance=lead)
        
        if form_p.is_valid() and form_l.is_valid():
            form_p.save()
            form_l.save()
            # Aquí podrías guardar observaciones si el campo viene en el POST
            return redirect('listar_leads')
    else:
        # Pre-llenamos con los datos actuales
        form_p = EditarLeadForm(instance=persona, initial={'numero_documento_persona': persona.numero_documento_persona})
        form_l = EditarEstadoLeadForm(instance=lead)

    return render(request, 'leads/editar_lead.html', {
        'form_p': form_p,
        'form_l': form_l,
        'lead': lead,
        'obs': obs
    })