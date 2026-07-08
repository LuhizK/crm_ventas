# leads/forms/captura_inicial.py
from django import forms

class CapturaTelefonoForm(forms.Form):
    # Campo 1: El número a buscar/marcar
    numero_marcado = forms.CharField(
        max_length=20,
        label="Número de Teléfono",
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg', 
            'placeholder': 'Ej. 3001234567',
            'autofocus': 'autofocus' # Pone el cursor aquí automáticamente
        })
    )
    
    # Campo 2: La observación inicial de la llamada
    observacion = forms.CharField(
        required=False, # No es obligatorio si apenas va a marcar
        label="Observación Inicial",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Notas sobre la llamada inicial (opcional)'
        })
    )

    # Método de validación interna: Limpiar el teléfono
    def clean_numero_marcado(self):
        numero = self.cleaned_data.get('numero_marcado')
        numero_limpio = numero.strip()
        if not numero_limpio.isdigit():
            raise forms.ValidationError("El número telefónico solo debe contener dígitos.")
            
        return numero_limpio