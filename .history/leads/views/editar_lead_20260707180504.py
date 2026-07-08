from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from ..models import Leads, Persona, Observaciones, PlataformaRiesgo, AcuerdoPago
from ..forms.editar_lead import EditarLeadForm, EditarEstadoLeadForm

def editar_lead(request, id_lead):
    lead = get_object_or_404(Leads, id_lead=id_lead)
    persona = lead.id_persona
    
    plataformas = PlataformaRiesgo.objects.filter(id_lead=lead)
    acuerdo = AcuerdoPago.objects.filter(id_lead=lead).first()

    historial_obs = Observaciones.objects.filter(id_lead=lead).order_by('-fecha_registro')

    if request.method == 'POST':
        # Instanciamos formularios con los datos del POST
        form_p = EditarLeadForm(request.POST, instance=persona)
        form_l = EditarEstadoLeadForm(request.POST, instance=lead)
        
        # Capturamos la nueva nota
        nueva_obs_texto = request.POST.get('nueva_observacion', '').strip()
        
        if form_p.is_valid() and form_l.is_valid():
            with transaction.atomic():
                form_p.save()
                form_l.save()
                
                # Si escribió algo, creamos una nueva observación en el historial
                if nueva_obs_texto:
                    Observaciones.objects.create(
                        id_lead=lead,
                        observacion=nueva_obs_texto
                    )
            return redirect('editar_lead', id_lead=lead.id_lead)
    else:
        # GET: Mostramos los formularios con datos actuales
        form_p = EditarLeadForm(instance=persona)
        form_l = EditarEstadoLeadForm(instance=lead)

    return render(request, 'leads/editar_lead.html', {
        'form_p': form_p,
        'form_l': form_l,
        'lead': lead,
        'historial_obs': historial_obs
    })