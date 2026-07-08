from django import forms
from ..models import Leads, Persona

class EditarLeadForm(forms.ModelForm):
    # Protegemos campos clave
    numero_documento_persona = forms.CharField(label="Documento", disabled=True)
    
    class Meta:
        model = Persona
        fields = ['nombres', 'apellidos', 'numero_documento_persona', 'direccion_persona', 'correo_persona']

class EditarEstadoLeadForm(forms.ModelForm):
    class Meta:
        model = Leads
        fields = ['estado_lead']