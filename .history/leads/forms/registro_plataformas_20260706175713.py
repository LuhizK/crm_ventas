from django import forms

class PlataformasReporteForm(forms.Form):
    # --- 1. DATACRÉDITO ---
    datacredito_usuario = forms.CharField(label="Usuario", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    datacredito_password = forms.CharField(label="Contraseña", required=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}))
    # CAMBIO AQUÍ: Usamos FileInput en lugar de ClearableFileInput
    datacredito_archivos = forms.FileField(label="Reportes (Múltiples PDF/Img)", required=False, widget=forms.FileInput(attrs={'class': 'form-control', 'multiple': True}))
    datacredito_notas = forms.CharField(label="Notas Adicionales", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))

    # --- 2. EQUIFAX ---
    equifax_usuario = forms.CharField(label="Usuario", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    equifax_password = forms.CharField(label="Contraseña", required=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}))
    equifax_archivos = forms.FileField(label="Reportes (Múltiples PDF/Img)", required=False, widget=forms.FileInput(attrs={'class': 'form-control', 'multiple': True}))
    equifax_notas = forms.CharField(label="Notas Adicionales", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))

    # --- 3. TRANSUNION ---
    transunion_usuario = forms.CharField(label="Usuario", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    transunion_password = forms.CharField(label="Contraseña", required=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}))
    transunion_archivos = forms.FileField(label="Reportes (Múltiples PDF/Img)", required=False, widget=forms.FileInput(attrs={'class': 'form-control', 'multiple': True}))
    transunion_notas = forms.CharField(label="Notas Adicionales", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))

    # --- 4. EXPERIAN ---
    experian_usuario = forms.CharField(label="Usuario", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    experian_password = forms.CharField(label="Contraseña", required=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}))
    experian_archivos = forms.FileField(label="Reportes (Múltiples PDF/Img)", required=False, widget=forms.FileInput(attrs={'class': 'form-control', 'multiple': True}))
    experian_notas = forms.CharField(label="Notas Adicionales", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))

    # --- 5. CIFIN ---
    cifin_usuario = forms.CharField(label="Usuario", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cifin_password = forms.CharField(label="Contraseña", required=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}))
    cifin_archivos = forms.FileField(label="Reportes (Múltiples PDF/Img)", required=False, widget=forms.FileInput(attrs={'class': 'form-control', 'multiple': True}))
    cifin_notas = forms.CharField(label="Notas Adicionales", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))

    # --- 6. OTRA PLATAFORMA ---
    otro_nombre = forms.CharField(label="Nombre de la Plataforma", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. LexisNexis'}))
    otro_usuario = forms.CharField(label="Usuario", required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    otro_password = forms.CharField(label="Contraseña", required=False, widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}))
    otro_archivos = forms.FileField(label="Reportes (Múltiples PDF/Img)", required=False, widget=forms.FileInput(attrs={'class': 'form-control', 'multiple': True}))
    otro_notas = forms.CharField(label="Notas Adicionales", required=False, widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 2}))