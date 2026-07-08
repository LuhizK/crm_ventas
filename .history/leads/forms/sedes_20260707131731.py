from django import forms
from ..models import Sede, Persona

class SedeForm(forms.ModelForm):
    id_responsable = forms.ModelChoiceField(
        queryset=Persona.objects.all(), 
        label="Responsable de la Sede",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    class Meta:
        model = Sede
        fields = ['nombre_sede', 'direccion_sede', 'id_responsable', 'correo_sede', 'telefono_sede']
        widgets = {
            'nombre_sede': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion_sede': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_sede': forms.EmailInput(attrs={'class': 'form-control'}),
            'telefono_sede': forms.TextInput(attrs={'class': 'form-control'}),
        }