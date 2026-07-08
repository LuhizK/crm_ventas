from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from ..models import Leads, Persona, Observaciones, Telefonos, PlataformaRiesgo, AcuerdoPago
from ..forms.editar_lead import EditarLeadForm

def editar_lead(request, id_lead):
    lead = get_object_or_404(Leads, id_lead=id_lead)
    persona = lead.id_persona
    
    # Cargar datos relacionados
    telefonos = Telefonos.objects.filter(id_persona=persona)
    plataformas = PlataformaRiesgo.objects.filter(id_lead=lead)
    acuerdo = AcuerdoPago.objects.filter(id_lead=lead).first()
    historial_obs = Observaciones.objects.filter(id_lead=lead).order_by('-fecha_registro')

    if request.method == 'POST':
        form_p = EditarLeadForm(request.POST, instance=persona)
        nueva_obs = request.POST.get('nueva_observacion', '').strip()
        
        if form_p.is_valid():
            with transaction.atomic():
                form_p.save()
                if nueva_obs:
                    Observaciones.objects.create(id_lead=lead, observacion=nueva_obs)
            return redirect('editar_lead', id_lead=lead.id_lead)
    else:
        form_p = EditarLeadForm(instance=persona)

    return render(request, 'leads/editar_lead.html', {
        'form_p': form_p,
        'lead': lead,
        'persona': persona,
        'telefonos': telefonos,
        'plataformas': plataformas,
        'acuerdo': acuerdo,
        'historial_obs': historial_obs
    })