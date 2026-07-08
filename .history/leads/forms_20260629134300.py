# leads/forms.py
from django import forms
from .models import Trabajador

class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        # Aquí definimos qué campos queremos mostrar en el formulario
        fields = ['id_persona', 'id_sede', 'id_cargo']
        
        # Opcional: agregamos clases de CSS para que se vea bonito con Bootstrap después
        widgets = {
            'id_persona': forms.Select(attrs={'class': 'form-control'}),
            'id_sede': forms.Select(attrs={'class': 'form-control'}),
            'id_cargo': forms.Select(attrs={'class': 'form-control'}),
        }