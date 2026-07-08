from django.shortcuts import render
from ..models import Ciudad, Sede, Trabajador, Leads

def panel_control(request):
    tiene_ciudades = Ciudad.objects.exists()
    tiene_sedes = Sede.objects.exists()
    tiene_trabajadores = Trabajador.objects.exists()

    # REGLA DE NEGOCIO: La operación de leads solo es posible si hay configuración base
    operacion_habilitada = tiene_ciudades and tiene_sedes and tiene_trabajadores

    contexto = {
        'total_ciudades': Ciudad.objects.count(),
        'total_sedes': Sede.objects.count(),
        'total_trabajadores': Trabajador.objects.count(),
        'total_leads': Leads.objects.count(),

        'tiene_ciudades': tiene_ciudades,
        'tiene_sedes': tiene_sedes,
        'tiene_trabajadores': tiene_trabajadores,
        'operacion_habilitada': operacion_habilitada,
    }

    return render(request, 'leads/panel_control.html', contexto)