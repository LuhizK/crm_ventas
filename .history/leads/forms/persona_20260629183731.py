# leads/forms/persona.py
from django import forms
from ..models import Persona

class PersonaForm(forms.ModelForm):
    # 1. Definimos las opciones como una lista de tuplas
    TIPO_DOCUMENTO_CHOICES = [
        ('CC', 'Cédula de Ciudadanía'),
        ('TI', 'Tarjeta de Identidad'),
        ('CE', 'Cédula de Extranjería'),
        ('PT', 'Pasaporte'),
        ('NIT', 'NIT'),
    ]

    # 2. Sobrescribimos el campo para que sea un ChoiceField (dropdown)
    tipo_documento_persona = forms.ChoiceField(
        choices=TIPO_DOCUMENTO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Persona
        fields = [
            'nombres', 'apellidos', 'tipo_documento_persona', 
            'numero_documento_persona', 'fecha_expedicion_persona', 
            'fecha_nacimiento_persona', 'genero_persona', 
            'correo_persona', 'direccion_persona', 
            'complemento_persona', 'barrio_persona', 'id_ciudad'
        ]
        # 3. Mantenemos el resto de widgets igual
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            # ... (los otros widgets se mantienen)
            'fecha_expedicion_persona': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_nacimiento_persona': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'genero_persona': forms.Select(choices=[('M', 'Masculino'), ('F', 'Femenino')], attrs={'class': 'form-select'}),
            'correo_persona': forms.EmailInput(attrs={'class': 'form-control'}),
            'direccion_persona': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento_persona': forms.TextInput(attrs={'class': 'form-control'}),
            'barrio_persona': forms.TextInput(attrs={'class': 'form-control'}),
            'id_ciudad': forms.Select(attrs={'class': 'form-select'}),
        }
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