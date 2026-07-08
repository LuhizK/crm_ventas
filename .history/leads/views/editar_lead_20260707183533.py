from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.db.models import Sum
from ..models import Leads, Persona, Observaciones, Telefonos, UsuarioReporte, AcuerdoPago, FechasPago
from ..forms.editar_lead import EditarLeadForm

def editar_lead(request, id_lead):
    lead = get_object_or_404(Leads, id_lead=id_lead)
    persona = lead.id_persona
    
    # Datos relacionados
    telefonos = Telefonos.objects.filter(id_persona=persona)
    reportes = UsuarioReporte.objects.filter(id_lead=lead)
    acuerdo = lead.id_acuerdo_pago
    historial_obs = Observaciones.objects.filter(id_lead=lead).order_by('-fecha_registro')
    
    # Lógica Financiera
    cronograma = []
    total_pagado = 0
    deuda_pendiente = 0
    
    if acuerdo:
        cronograma = FechasPago.objects.filter(id_acuerdo_pago=acuerdo).order_by('fecha_pago')
        total_pagado = cronograma.aggregate(Sum('valor_pagado'))['valor_pagado__sum'] or 0
        deuda_pendiente = acuerdo.valor_total_acuerdo_pago - total_pagado

    if request.method == 'POST':
        form_p = EditarLeadForm(request.POST, instance=persona)
        nueva_obs = request.POST.get('nueva_observacion', '').strip()
        
        if form_p.is_valid():
            with transaction.atomic():
                form_p.save()
                if nueva_obs:
                    Observaciones.objects.create(
                        id_lead=lead,
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
        'cronograma': cronograma,
        'total_pagado': total_pagado,
        'deuda_pendiente': deuda_pendiente,
        'historial_obs': historial_obs
    })