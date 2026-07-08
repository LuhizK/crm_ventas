from django import forms

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput(attrs={'class': 'form-control'}))
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class PlataformasReporteForm(forms.Form):
    # --- 1. DATACRÉDITO ---
    datacredito_usuario = forms.CharField(label="Usuario", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    datacredito_password = forms.CharField(label="Contraseña", required=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}))
    # Usamos nuestra nueva superclase
    datacredito_archivos = MultipleFileField(label="Reportes (Múltiples PDF/Img)", required=False)
    datacredito_notas = forms.CharField(label="Notas Adicionales", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))

    # --- 2. EQUIFAX ---
    equifax_usuario = forms.CharField(label="Usuario", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    equifax_password = forms.CharField(label="Contraseña", required=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}))
    equifax_archivos = MultipleFileField(label="Reportes (Múltiples PDF/Img)", required=False)
    equifax_notas = forms.CharField(label="Notas Adicionales", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))

    # --- 3. TRANSUNION ---
    transunion_usuario = forms.CharField(label="Usuario", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    transunion_password = forms.CharField(label="Contraseña", required=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}))
    transunion_archivos = MultipleFileField(label="Reportes (Múltiples PDF/Img)", required=False)
    transunion_notas = forms.CharField(label="Notas Adicionales", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))

    # --- 4. EXPERIAN ---
    experian_usuario = forms.CharField(label="Usuario", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    experian_password = forms.CharField(label="Contraseña", required=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}))
    experian_archivos = MultipleFileField(label="Reportes (Múltiples PDF/Img)", required=False)
    experian_notas = forms.CharField(label="Notas Adicionales", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))

    # --- 5. CIFIN ---
    cifin_usuario = forms.CharField(label="Usuario", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cifin_password = forms.CharField(label="Contraseña", required=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}))
    cifin_archivos = MultipleFileField(label="Reportes (Múltiples PDF/Img)", required=False)
    cifin_notas = forms.CharField(label="Notas Adicionales", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))

    # --- 6. OTRA PLATAFORMA ---
    otro_nombre = forms.CharField(label="Nombre de la Plataforma", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. LexisNexis'}))
    otro_usuario = forms.CharField(label="Usuario", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    otro_password = forms.CharField(label="Contraseña", required=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}))
    otro_archivos = MultipleFileField(label="Reportes (Múltiples PDF/Img)", required=False)
    otro_notas = forms.CharField(label="Notas Adicionales", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))