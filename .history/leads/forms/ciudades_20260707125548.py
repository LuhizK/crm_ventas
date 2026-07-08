from django import forms
from ..models import Ciudad

class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ['ciudad'] # Le decimos qué columnas de la base de datos incluir
        labels = {
            'ciudad': 'Nombre de la Ciudad'
        }
        widgets = {
            'ciudad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Bogotá'})
        }