from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from ..models import Leads, Persona, Observaciones, Telefonos, UsuarioReporte, AcuerdoPago
from ..forms.editar_lead import EditarLeadForm

def editar_lead(request, id_lead):
    # Obtenemos los objetos necesarios
    lead = get_object_or_404(Leads, id_lead=id_lead)
    persona = lead.id_persona
    
    # Carga de datos relacionados según tu models.py
    telefonos = Telefonos.objects.filter(id_persona=persona)
    reportes = UsuarioReporte.objects.filter(id_lead=lead)
    acuerdo = lead.id_acuerdo_pago # ForeignKey directa en el modelo Leads
    historial_obs = Observaciones.objects.filter(id_lead=lead).order_by('-fecha_registro')

    if request.method == 'POST':
        form_p = EditarLeadForm(request.POST, instance=persona)
        nueva_obs = request.POST.get('nueva_observacion', '').strip()
        
        if form_p.is_valid():
            with transaction.atomic():
                form_p.save()
                if nueva_obs:
                    Observaciones.objects.create(
                        id_lead=lead,
                        id_trabajador=None, # Ajustar si necesitas asignar trabajador
                        observacion=nueva_obs,
                        fecha_registro=lead.fecha_creacion 
                    )
            return redirect('editar_lead', id_lead=lead.id_lead)
    else:
        form_p = EditarLeadForm(instance=persona)

    return render(request, 'leads/editar_lead.html', {
        'form_p': form_p,
        'lead': lead,
        'persona': persona,
        'telefonos': telefonos,
        'reportes': reportes,
        'acuerdo': acuerdo,
        'historial_obs': historial_obs
    })