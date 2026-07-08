from django.shortcuts import render
from ..models import Leads
from ..utils import es_sistema_operativo

def listar_leads(request):
    leads = Leads.objects.all().order_by('-fecha_creacion', '-hora_creacion')
    
    # Pasamos la bandera al HTML para decidir si mostramos el botón o un aviso
    contexto = {
        'leads': leads,
        'puede_crear': es_sistema_operativo()
    }
    return render(request, 'leads/listar_leads.html', contexto)