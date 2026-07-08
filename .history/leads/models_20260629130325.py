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


class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    ciudad = models.CharField(max_length=100)
    class Meta:
        managed = False
        db_table = 'ciudad'

class Sede(models.Model):
    id_sede = models.AutoField(primary_key=True)
    nombre_sede = models.CharField(max_length=100)
    id_responsable = models.ForeignKey(Persona, on_delete=models.SET_NULL, db_column='id_responsable', null=True)
    class Meta:
        managed = False
        db_table = 'sede'

class Trabajador(models.Model):
    id_trabajador = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='id_persona')
    id_sede = models.ForeignKey(Sede, on_delete=models.SET_NULL, db_column='id_sede', null=True)
    class Meta:
        managed = False
        db_table = 'trabajador'

class Telefonos(models.Model):
    id_telefono = models.AutoField(primary_key=True)
    numero_telefono = models.CharField(max_length=20)
    id_persona = models.ForeignKey(Persona, on_delete=models.CASCADE, db_column='id_persona')
    class Meta:
        managed = False
        db_table = 'telefonos'