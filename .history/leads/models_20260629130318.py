from django.db import models

# Tabla Persona - La base de todo
class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    numero_documento_persona = models.CharField(max_length=20, unique=True)

    class Meta:
        managed = False  # ESTO ES CLAVE: Le dice a Django "no toques mi BD, ya existe"
        db_table = 'persona'

# Tabla Leads - Relacionada con Persona
class Leads(models.Model):
    id_lead = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='id_persona')
    estado_lead = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'leads'
        
        