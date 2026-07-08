from django.contrib import admin
from .models import Persona, Leads, Ciudad, Trabajador, AcuerdoPago # Importa las que necesites ver

# Registramos las tablas para verlas en el admin
admin.site.register(Persona)
admin.site.register(Leads)
admin.site.register(Ciudad)
admin.site.register(Trabajador)
admin.site.register(AcuerdoPago)
