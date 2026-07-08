# leads/forms/captura_inicial.py
from django import forms

class CapturaTelefonoForm(forms.Form):
    # Variables de control de entorno (Fácilmente modificables)
    LONGITUD_MINIMA = 10
    LONGITUD_MAXIMA = 10

    # Campo 1: El número a buscar/marcar
    numero_marcado = forms.CharField(
        max_length=LONGITUD_MAXIMA,
        min_length=LONGITUD_MINIMA, # Esto activa una validación nativa en el navegador
        label="Número de Teléfono",
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg', 
            'placeholder': 'Ej. 3001234567',
            'autofocus': 'autofocus'
        })
    )
    
    # Campo 2: La observación inicial de la llamada
    observacion = forms.CharField(
        required=False, 
        label="Observación Inicial",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 3,
            'placeholder': 'Notas sobre la llamada inicial (opcional)'
        })
    )

    # Método de validación interna: Limpiar y verificar longitud exacta
    def clean_numero_marcado(self):
        numero = self.cleaned_data.get('numero_marcado')
        numero_limpio = numero.strip()
        
        # 1. Validación de tipo de dato (Solo números)
        if not numero_limpio.isdigit():
            raise forms.ValidationError("El número telefónico solo debe contener dígitos.")
        
        # 2. Validación estricta de longitud (Regla de negocio)
        longitud_actual = len(numero_limpio)
        if longitud_actual < self.LONGITUD_MINIMA or longitud_actual > self.LONGITUD_MAXIMA:
            # Si el mínimo y máximo son iguales, el mensaje es estricto
            if self.LONGITUD_MINIMA == self.LONGITUD_MAXIMA:
                raise forms.ValidationError(f"El número debe tener exactamente {self.LONGITUD_MINIMA} dígitos. Ingresaste {longitud_actual}.")
            else:
                # Si hay un rango, el mensaje es flexible
                raise forms.ValidationError(f"El número debe tener entre {self.LONGITUD_MINIMA} y {self.LONGITUD_MAXIMA} dígitos.")
            
        return numero_limpio