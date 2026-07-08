from django import forms
from ..models import Persona

class PersonaNuevaForm(forms.ModelForm):
    # Campo para mostrar el teléfono bloqueado (sin que el asesor lo edite)
    telefono_referencia = forms.CharField(label="Teléfono Principal", disabled=True)

    class Meta:
        model = Persona
        fields = [
            'nombres', 'apellidos', 'tipo_documento_persona', 
            'numero_documento_persona', 'fecha_expedicion_persona', 
            'fecha_nacimiento_persona', 'genero_persona', 
            'correo_persona', 'direccion_persona', 'id_ciudad'
        ]
        # Widgets para que se vean bonitos con Bootstrap
        widgets = {
            'nombres': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_documento_persona': forms.TextInput(attrs={'class': 'form-control'}),
            # ... (puedes añadir el resto de clases CSS aquí)
        }