from django import forms
from ..models import Persona

class PersonaNuevaForm(forms.ModelForm):
    # Campo para referencia visual (Bloqueado)
    telefono_referencia = forms.CharField(label="Teléfono Principal", disabled=True)
    
    # Campo para la observación que viaja de vista en vista
    observacion_referencia = forms.CharField(
        label="Observación de la Llamada", 
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        disabled=False # Editable hasta que guarde el flujo final
    )

    class Meta:
        model = Persona
        fields = [
            'nombres', 'apellidos', 'tipo_documento_persona', 
            'numero_documento_persona', 'fecha_expedicion_persona', 
            'fecha_nacimiento_persona', 'genero_persona', 
            'correo_persona', 'direccion_persona', 'complemento_persona', 
            'barrio_persona', 'id_ciudad'
        ]
        # Aquí mapeamos los widgets para que todos tengan la clase 'form-control'
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_documento_persona': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_expedicion_persona': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fecha_nacimiento_persona': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'id_ciudad': forms.Select(attrs={'class': 'form-select'}),
            # ... agrega los otros campos necesarios
        }