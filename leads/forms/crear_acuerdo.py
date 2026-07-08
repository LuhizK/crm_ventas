from django import forms
from ..models import Servicios

class AcuerdoPagoForm(forms.Form):
    # --- SERVICIOS ---
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

    # --- FECHAS Y CUOTAS DE PAGO ---
    fecha_cuota_1 = forms.DateField(label="Fecha Cuota 1", required=True, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    valor_cuota_1 = forms.DecimalField(label="Valor Cuota 1 ($)", max_digits=10, decimal_places=2, required=True, widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))

    fecha_cuota_2 = forms.DateField(label="Fecha Cuota 2 (Opcional)", required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    valor_cuota_2 = forms.DecimalField(label="Valor Cuota 2 ($)", max_digits=10, decimal_places=2, required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))

    fecha_cuota_3 = forms.DateField(label="Fecha Cuota 3 (Opcional)", required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    valor_cuota_3 = forms.DecimalField(label="Valor Cuota 3 ($)", max_digits=10, decimal_places=2, required=False, widget=forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}))

    # --- HILO CONDUCTOR: OBSERVACIONES ---
    observacion_general = forms.CharField(
        label="Bitácora / Observaciones del Lead", 
        required=False, 
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Agrega notas sobre los servicios o fechas acordadas...'})
    )

    # --- MAGIA FINANCIERA CON BUCLES ---
    def clean(self):
        cleaned_data = super().clean()
        total_servicios = 0

        for i in [1, 2]:
            servicio = cleaned_data.get(f'servicio_{i}')
            valor = cleaned_data.get(f'valor_servicio_{i}')

            if servicio and not valor:
                self.add_error(f'valor_servicio_{i}', f"Debes ingresar el precio final para el Servicio {i}.")
            elif valor and not servicio:
                self.add_error(f'servicio_{i}', "Ingresaste un precio, pero no seleccionaste qué servicio es.")
            elif servicio and valor:
                if valor < servicio.precio_minimo or valor > servicio.precio_maximo:
                    self.add_error(f'valor_servicio_{i}', f"Rango no permitido. Debe estar entre ${servicio.precio_minimo} y ${servicio.precio_maximo}")
                else:
                    total_servicios += valor

        total_cuotas = sum(cleaned_data.get(f'valor_cuota_{i}') or 0 for i in [1, 2, 3])

        # Auditoría Contable
        if total_servicios > 0 and total_cuotas != total_servicios:
            raise forms.ValidationError(
                f"ERROR FINANCIERO: El total de los servicios es ${total_servicios}, pero la suma de las cuotas es ${total_cuotas}. "
                "Los montos deben coincidir exactamente para proceder."
            )

        cleaned_data['total_calculado'] = total_servicios

        return cleaned_data