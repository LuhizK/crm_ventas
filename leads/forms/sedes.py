from django import forms
from ..models import Sede, Persona

class PersonaChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        # Evita que aparezca 'Persona object (X)' en el select de HTML
        return f"{obj.nombres} {obj.apellidos}"

class SedeForm(forms.ModelForm):
    id_responsable = PersonaChoiceField(
        queryset=Persona.objects.all(),
        label="Responsable de la Sede",
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Sede
        fields = ['nombre_sede', 'direccion_sede', 'id_responsable', 'correo_sede', 'telefono_sede']
        labels = {
            'nombre_sede': 'Nombre de la Sede',
            'direccion_sede': 'Dirección Física',
            'correo_sede': 'Correo Electrónico',
            'telefono_sede': 'Teléfono de Contacto',
        }
        widgets = {
            'nombre_sede': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Sede Norte'}),
            'direccion_sede': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Calle 100 #15-20'}),
            'correo_sede': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ej. norte@deudoor.com'}),
            'telefono_sede': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 601234567'}),
        }