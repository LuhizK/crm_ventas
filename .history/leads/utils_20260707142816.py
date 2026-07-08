from ..models import Ciudad, Sede, Trabajador

def sistema_operativo():
    """Retorna True solo si existen los requisitos mínimos para operar."""
    return Ciudad.objects.exists() and Sede.objects.exists() and Trabajador.objects.exists()