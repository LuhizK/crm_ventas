from django import forms
from ..models import Trabajador, Persona, Sede, Cargo

class PersonaChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.nombres} {obj.apellidos} - {obj.numero_documento_persona or 'Sin Doc'}"

class SedeChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nombre_sede

class CargoChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nombre_cargo

class TrabajadorForm(forms.ModelForm):
    id_persona = PersonaChoiceField(
        queryset=Persona.objects.all(),
        label="Persona Vinculada (Datos Personales)",
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    id_sede = SedeChoiceField(
        queryset=Sede.objects.all(),
        label="Sede Asignada",
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    id_cargo = CargoChoiceField(
        queryset=Cargo.objects.all(),
        label="Cargo Operativo",
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Trabajador
        fields = ['id_persona', 'id_sede', 'id_cargo']