from django import forms
from ..models import Persona

class PersonaNuevaForm(forms.ModelForm):
    # Definición de opciones (hardcoded por ahora)
    TIPO_DOC_CHOICES = [
        ('', 'Seleccione...'),
        ('CC', 'Cédula de Ciudadanía'),
        ('CE', 'Cédula de Extranjería'),
        ('SSN', 'Social Security Number'),
        ('ITIN', 'ITIN Number'),
    ]

    telefono_referencia = forms.CharField(
        label="Teléfono Principal", 
        disabled=True, 
        required=False
    )
    observacion_referencia = forms.CharField(label="Observación de la Llamada", widget=forms.Textarea(attrs={'rows': 2}))
    
    # Sobrescribimos el tipo de documento para que sea una lista (Select)
    tipo_documento_persona = forms.ChoiceField(choices=TIPO_DOC_CHOICES, label="Tipo de Documento")

    class Meta:
        model = Persona
        fields = [
            'nombres', 'apellidos', 'tipo_documento_persona', 'numero_documento_persona', 
            'fecha_expedicion_persona', 'fecha_nacimiento_persona', 'genero_persona', 
            'correo_persona', 'direccion_persona', 'complemento_persona', 
            'barrio_persona', 'id_ciudad'
        ]
        widgets = {
            # Aplicamos la misma clase a todo para uniformar
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_documento_persona': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_expedicion_persona': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_nacimiento_persona': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'genero_persona': forms.Select(choices=[('', '---'), ('M', 'Masculino'), ('F', 'Femenino')], attrs={'class': 'form-select'}),
            'correo_persona': forms.EmailInput(attrs={'class': 'form-control'}),
            'direccion_persona': forms.TextInput(attrs={'class': 'form-control'}),
            'complemento_persona': forms.TextInput(attrs={'class': 'form-control'}),
            'barrio_persona': forms.TextInput(attrs={'class': 'form-control'}),
            'id_ciudad': forms.Select(attrs={'class': 'form-select'}),
        }