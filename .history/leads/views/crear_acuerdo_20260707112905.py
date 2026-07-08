from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.http import HttpResponse
from ..forms.crear_acuerdo import AcuerdoPagoForm
from ..models import Leads, AcuerdoPago, AcuerdoPagoDetalle, FechasPago, Observaciones

def crear_acuerdo_pago(request, id_lead):
    # 1. Traer datos del cliente (Lead y Observaciones)
    lead_actual = get_object_or_404(Leads, id_lead=id_lead)
    
    observacion_actual = Observaciones.objects.filter(id_lead=lead_actual).first()
    texto_obs_existente = observacion_actual.observacion if observacion_actual else ""

    if request.method == 'POST':
        form = AcuerdoPagoForm(request.POST)

        if form.is_valid():
            try:
                with transaction.atomic():
                    # 2. CREAR EL MAESTRO (El Recibo)
                    nuevo_acuerdo = AcuerdoPago.objects.create(
                        valor_total_acuerdo_pago=form.cleaned_data['total_calculado'],
                        observaciones_acuerdo_pago="Acuerdo generado desde flujo inicial."
                    )
                    
                    # 3. ENLAZAR EL ACUERDO AL LEAD
                    lead_actual.id_acuerdo_pago = nuevo_acuerdo
                    lead_actual.save()

                    # 4. CREAR EL DETALLE (Los Servicios)
                    for i in [1, 2]:
                        servicio = form.cleaned_data.get(f'servicio_{i}')
                        valor = form.cleaned_data.get(f'valor_servicio_{i}')
                        if servicio and valor:
                            AcuerdoPagoDetalle.objects.create(
                                id_acuerdo_pago=nuevo_acuerdo,
                                id_servicio=servicio,
                                valor_cobrado=valor
                            )

                    # 5. CREAR LAS CUOTAS (Fechas de Pago)
                    for i in [1, 2, 3]:
                        fecha = form.cleaned_data.get(f'fecha_cuota_{i}')
                        valor_cuota = form.cleaned_data.get(f'valor_cuota_{i}')
                        if fecha and valor_cuota:
                            FechasPago.objects.create(
                                id_acuerdo_pago=nuevo_acuerdo,
                                valor_fecha_pago=valor_cuota,
                                fecha_pago=fecha,
                                estado_pago='PENDIENTE'
                            )
                            
                    # 6. ACTUALIZAR OBSERVACIÓN GENERAL
                    nueva_obs = form.cleaned_data.get('observacion_general')
                    if observacion_actual and nueva_obs:
                        observacion_actual.observacion = nueva_obs
                        observacion_actual.save()

                    # Flujo terminado exitosamente
                    return redirect('captura_inicial') 

            except Exception as e:
                return HttpResponse(f"<h1>Error en la Base de Datos</h1><p>{str(e)}</p>")
        else:
            # Si clean() arroja error (ej. precio fuera de rango), recargamos el HTML con los errores
            return render(request, 'leads/crear_acuerdo.html', {'form': form, 'lead': lead_actual})

    else:
        # GET: Cargar formulario vacío inyectando la observación anterior
        form = AcuerdoPagoForm(initial={'observacion_general': texto_obs_existente})

    return render(request, 'leads/crear_acuerdo.html', {'form': form, 'lead': lead_actual})