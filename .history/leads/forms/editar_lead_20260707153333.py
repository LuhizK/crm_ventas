from django import forms
from ..models import Leads, Persona, Observaciones

class EdicionMaestraForm(forms.ModelForm):
    # Campos de Persona
    nombres = forms.CharField(label="Nombres", widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellidos = forms.CharField(label="Apellidos", widget=forms.TextInput(attrs={'class': 'form-control'}))
    numero_documento_persona = forms.CharField(label="Documento", disabled=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Persona
        fields = ['nombres', 'apellidos', 'numero_documento_persona', 'direccion_persona', 'correo_persona']

class EstadoYReporteForm(forms.ModelForm):
    class Meta:
        model = Leads
        # Incluye aquí todos los campos de central de riesgo que tienes en tu modelo
        fields = ['estado_lead', 'reporte_datacredito', 'reporte_cifin', 'score_riesgo']
        widgets = {
            'estado_lead': forms.Select(attrs={'class': 'form-select'}),
            'reporte_datacredito': forms.TextInput(attrs={'class': 'form-control'}),
            'reporte_cifin': forms.TextInput(attrs={'class': 'form-control'}),
            'score_riesgo': forms.NumberInput(attrs={'class': 'form-control'}),
        }