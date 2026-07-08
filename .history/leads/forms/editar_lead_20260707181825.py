from django import forms
from ..models import Persona

class EditarLeadForm(forms.ModelForm):
    # Protegemos el ID (Documento) para que no sea editable
    numero_documento_persona = forms.CharField(label="Documento de Identidad", disabled=True)

    class Meta:
        model = Persona
        fields = [
            'nombres', 'apellidos', 'numero_documento_persona', 
            'direccion_persona', 'correo_persona', 
            'telefono_principal', 'telefono_adicional'
        ]
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_persona': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_persona': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono_principal': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_adicional': forms.TextInput(attrs={'class': 'form-control'}),
        }