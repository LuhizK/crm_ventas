from django.shortcuts import render
from ..models import Ciudad, Sede, Trabajador, Leads

def panel_control(request):
    tiene_ciudades = Ciudad.objects.exists()
    tiene_sedes = Sede.objects.exists()
    tiene_trabajadores = Trabajador.objects.exists()

    # REGLA DE NEGOCIO: Solo se puede operar si existen los 3 prerrequisitos
    operacion_habilitada = tiene_ciudades and tiene_sedes and tiene_trabajadores

    # CONTADORES PARA EL DASHBOARD: Datos estadísticos para el instructor
    contexto = {
        'total_ciudades': Ciudad.objects.count(),
        'total_sedes': Sede.objects.count(),
        'total_trabajadores': Trabajador.objects.count(),
        'total_leads': Leads.objects.count(),
        
        # Banderas de control de interfaz
        'tiene_ciudades': tiene_ciudades,
        'tiene_sedes': tiene_sedes,
        'tiene_trabajadores': tiene_trabajadores,
        'operacion_habilitada': operacion_habilitada,
    }

    return render(request, 'leads/panel_control.html', contexto)