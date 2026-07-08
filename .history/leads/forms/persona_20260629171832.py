# leads/forms/persona.py
from django import forms
from ..models import Persona

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        # Incluimos todos los campos que tienes en tu DDL de la tabla 'persona'
        fields = [
            'nombres', 'apellidos', 'tipo_documento_persona', 
            'numero_documento_persona', 'fecha_expedicion_persona', 
            'fecha_nacimiento_persona', 'genero_persona', 
            'correo_persona', 'direccion_persona', 
            'complemento_persona', 'barrio_persona', 'id_ciudad'
        ]
        # Agregamos clases de Bootstrap para que el formulario se vea profesional
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_documento_persona': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_documento_persona': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_expedicion_persona': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_nacimiento_persona': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'genero_persona': forms.TextInput(attrs={'class': 'form-control'}),
            'correo_persona': forms.EmailInput(attrs={'class': 'form-control'}),
            'direccion_persona': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento_persona': forms.TextInput(attrs={'class': 'form-control'}),
            'barrio_persona': forms.TextInput(attrs={'class': 'form-control'}),
            'id_ciudad': forms.Select(attrs={'class': 'form-select'}),
        }