from django import forms
from ..models import Persona, Leads

class EditarLeadForm(forms.ModelForm):
    numero_documento_persona = forms.CharField(label="Documento", disabled=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = Persona
        fields = ['nombres', 'apellidos', 'numero_documento_persona', 'direccion_persona', 'correo_persona']
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_persona': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_persona': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class EditarEstadoLeadForm(forms.ModelForm):
    class Meta:
        model = Leads
        fields = []