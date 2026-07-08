from django import forms
from ..models import Servicios

class AcuerdoPagoForm(forms.Form):
    servicio_1 = forms.ModelChoiceField(
        queryset=Servicios.objects.filter(estado='ACTIVO'),
        label="Servicio Principal",
        required=True,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    valor_servicio_1 = forms.DecimalField(
        label="Precio Cobrado ($)",
        max_digits=10, decimal_places=2,
        required=True,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})
    )

    servicio_2 = forms.ModelChoiceField(
        queryset=Servicios.objects.filter(estado='ACTIVO'),
        label="Servicio Secundario (Opcional)",
        required=False,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    valor_servicio_2 = forms.DecimalField(
        label="Precio Cobrado ($)",
        max_digits=10, decimal_places=2,
        required=False,
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})
    )


    fecha_cuota_1 = forms.DateField(
        label="Fecha Cuota 1", 
        required=True, 
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    valor_cuota_1 = forms.DecimalField(
        label="Valor Cuota 1 ($)", 
        max_digits=10, decimal_places=2, 
        required=True, 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})
    )

    fecha_cuota_2 = forms.DateField(
        label="Fecha Cuota 2 (Opcional)", 
        required=False, 
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    valor_cuota_2 = forms.DecimalField(
        label="Valor Cuota 2 ($)", 
        max_digits=10, decimal_places=2, 
        required=False, 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})
    )

    fecha_cuota_3 = forms.DateField(
        label="Fecha Cuota 3 (Opcional)", 
        required=False, 
        widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'})
    )
    valor_cuota_3 = forms.DecimalField(
        label="Valor Cuota 3 ($)", 
        max_digits=10, decimal_places=2, 
        required=False, 
        widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'})
    )

    observacion_general = forms.CharField(
        label="Bitácora / Observaciones del Lead", 
        required=False, 
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Agrega notas sobre los servicios o fechas acordadas...'})
    )
    
    def clean(self):
        cleaned_data = super().clean()
        
        s1 = cleaned_data.get('servicio_1')
        v1 = cleaned_data.get('valor_servicio_1')
        s2 = cleaned_data.get('servicio_2')
        v2 = cleaned_data.get('valor_servicio_2')

        total_servicios = 0

        # Validar reglas del Servicio 1
        if s1 and not v1:
            self.add_error('valor_servicio_1', "Debes ingresar el precio final para el Servicio 1.")
        elif s1 and v1:
            if v1 < s1.precio_minimo or v1 > s1.precio_maximo:
                self.add_error('valor_servicio_1', f"Rango no permitido. Debe estar entre ${s1.precio_minimo} y ${s1.precio_maximo}")
            else:
                total_servicios += v1

        # Validar reglas del Servicio 2
        if s2 and not v2:
            self.add_error('valor_servicio_2', "Debes ingresar el precio final para el Servicio 2.")
        elif v2 and not s2:
            self.add_error('servicio_2', "Ingresaste un precio, pero no seleccionaste qué servicio es.")
        elif s2 and v2:
            if v2 < s2.precio_minimo or v2 > s2.precio_maximo:
                self.add_error('valor_servicio_2', f"Rango no permitido. Debe estar entre ${s2.precio_minimo} y ${s2.precio_maximo}")
            else:
                total_servicios += v2

        # Validar cruce contable (Total Servicios vs Total Cuotas)
        vc1 = cleaned_data.get('valor_cuota_1') or 0
        vc2 = cleaned_data.get('valor_cuota_2') or 0
        vc3 = cleaned_data.get('valor_cuota_3') or 0
        
        total_cuotas = vc1 + vc2 + vc3

        # Si hay venta, la suma de las partes debe ser exacta
        if total_servicios > 0 and total_cuotas != total_servicios:
            raise forms.ValidationError(
                f"ERROR FINANCIERO: El total de los servicios es ${total_servicios}, pero la suma de las cuotas es ${total_cuotas}. "
                "Los montos deben coincidir exactamente para proceder."
            )

        return cleaned_data