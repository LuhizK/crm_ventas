from .models import Ciudad, Sede, Trabajador

def es_sistema_operativo():
    """
    Retorna True solo si existen los requisitos mínimos para operar un lead.
    """
    return Ciudad.objects.exists() and Sede.objects.exists() and Trabajador.objects.exists()