from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from django.http import HttpResponse
from ..forms.registro_plataformas import PlataformasReporteForm
from ..models import Leads, UsuarioReporte, ReporteGrafico

def registro_plataformas(request, id_lead):
    lead_actual = get_object_or_404(Leads, id_lead=id_lead)

    if request.method == 'POST':
        form = PlataformasReporteForm(request.POST, request.FILES)

        if form.is_valid():
            try:
                with transaction.atomic():
                    plataformas = ['datacredito', 'equifax', 'transunion', 'experian', 'cifin', 'otro']
                    
                    for prefijo in plataformas:
                        usuario = form.cleaned_data.get(f'{prefijo}_usuario')
                        password = form.cleaned_data.get(f'{prefijo}_password')
                        notas = form.cleaned_data.get(f'{prefijo}_notas')
                        
                        nombre_plataforma = form.cleaned_data.get('otro_nombre') if prefijo == 'otro' else prefijo.upper()
                        
                        if usuario or password or notas:
                            UsuarioReporte.objects.create(
                                id_lead=lead_actual,
                                usuario_reporte=usuario,
                                password_reporte=password,
                                plataforma_reporte=nombre_plataforma,
                                descripcion_reporte=notas
                            )
                        
                        archivos_subidos = request.FILES.getlist(f'{prefijo}_archivos')
                        
                        for archivo in archivos_subidos:
                            ReporteGrafico.objects.create(
                                id_lead=lead_actual,
                                documento_reporte_grafico=archivo, # Django guarda el archivo en 'media/' y la ruta en DB
                                tipo_reporte_grafico=nombre_plataforma
                            )

                    # Si todo sale bien, podríamos redirigir a un dashboard o al siguiente paso.
                    # Por ahora lo mandaremos a la pantalla inicial como confirmación de fin de flujo.
                    return redirect('captura_inicial')

            except Exception as e:
                return HttpResponse(f"<h1>Error en la Base de Datos</h1><p>{str(e)}</p>")
        else:
            return HttpResponse(f"<h1>Error en el Formulario</h1><p>{form.errors}</p>")

    else:
        # Si es un GET, simplemente mostramos el formulario vacío
        form = PlataformasReporteForm()

    # Le pasamos el 'lead_actual' al HTML por si quieres mostrar el nombre del cliente en pantalla
    return render(request, 'leads/registro_plataformas.html', {'form': form, 'lead': lead_actual})