from django.db import models


class AcuerdoPago(models.Model):
    id_acuerdo_pago = models.AutoField(primary_key=True)
    valor_total_acuerdo_pago = models.DecimalField(max_digits=15, decimal_places=2)
    observaciones_acuerdo_pago = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acuerdo_pago'


class Cargo(models.Model):
    id_cargo = models.AutoField(primary_key=True)
    nombre_cargo = models.CharField(unique=True, max_length=100)
    descripcion_cargo = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cargo'


class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    ciudad = models.CharField(unique=True, max_length=100)

    # Añade esto justo debajo de los campos:
    def __str__(self):
        return self.ciudad # Esto le dice a Django: "Muestra el nombre de la ciudad"

    class Meta:
        managed = False
        db_table = 'ciudad'


class FechasPago(models.Model):
    id_fecha_pago = models.AutoField(primary_key=True)
    id_acuerdo_pago = models.ForeignKey(AcuerdoPago, models.DO_NOTHING, db_column='id_acuerdo_pago')
    valor_fecha_pago = models.DecimalField(max_digits=15, decimal_places=2)
    fecha_pago = models.DateField()
    estado_pago = models.CharField(max_length=25, blank=True, null=True)
    valor_pagado = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    fecha_pagado = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fechas_pago'


class Leads(models.Model):
    id_lead = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey('Persona', models.DO_NOTHING, db_column='id_persona')
    id_trabajador = models.ForeignKey('Trabajador', models.DO_NOTHING, db_column='id_trabajador')
    id_contrato = models.ForeignKey('MotivoContrato', models.DO_NOTHING, db_column='id_contrato', blank=True, null=True)
    id_acuerdo_pago = models.ForeignKey(AcuerdoPago, models.DO_NOTHING, db_column='id_acuerdo_pago', blank=True, null=True)
    estado_lead = models.CharField(max_length=20, blank=True, null=True)
    fecha_creacion = models.DateField(blank=True, null=True)
    hora_creacion = models.TimeField(blank=True, null=True)
    estado_flujo = models.CharField(max_length=50, default='NUEVO') # El nuevo campo tipo ENUM

    class Meta:
        managed = False
        db_table = 'leads'


class MotivoContrato(models.Model):
    id_contrato = models.AutoField(primary_key=True)
    motivo_contrato = models.CharField(unique=True, max_length=200)

    class Meta:
        managed = False
        db_table = 'motivo_contrato'


class Observaciones(models.Model):
    id_observaciones = models.AutoField(primary_key=True)
    id_lead = models.ForeignKey(Leads, models.DO_NOTHING, db_column='id_lead')
    id_trabajador = models.ForeignKey('Trabajador', models.DO_NOTHING, db_column='id_trabajador', blank=True, null=True)
    observacion = models.TextField()
    motivo_finalizacion_llamada = models.CharField(max_length=200, blank=True, null=True)
    estado_llamada = models.CharField(max_length=50, blank=True, null=True)
    fecha_registro = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'observaciones'


class Persona(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    tipo_documento_persona = models.CharField(max_length=5, blank=True, null=True)
    numero_documento_persona = models.CharField(unique=True, max_length=20, blank=True, null=True)
    fecha_expedicion_persona = models.DateField(blank=True, null=True)
    fecha_nacimiento_persona = models.DateField(blank=True, null=True)
    genero_persona = models.CharField(max_length=20, blank=True, null=True)
    correo_persona = models.CharField(max_length=100, blank=True, null=True)
    direccion_persona = models.CharField(max_length=150, blank=True, null=True)
    complemento_persona = models.CharField(max_length=100, blank=True, null=True)
    barrio_persona = models.CharField(max_length=100, blank=True, null=True)
    id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='id_ciudad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'persona'


class ReporteGrafico(models.Model):
    id_reporte_grafico = models.AutoField(primary_key=True)
    id_lead = models.ForeignKey(Leads, models.DO_NOTHING, db_column='id_lead')
    documento_reporte_grafico = models.CharField(max_length=255, blank=True, null=True)
    tipo_reporte_grafico = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'reporte_grafico'


class Rol(models.Model):
    id_rol = models.AutoField(primary_key=True)
    nombre_rol = models.CharField(unique=True, max_length=100)
    descripcion_rol = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rol'


class Sede(models.Model):
    id_sede = models.AutoField(primary_key=True)
    nombre_sede = models.CharField(max_length=100)
    direccion_sede = models.CharField(max_length=150, blank=True, null=True)
    id_responsable = models.ForeignKey(Persona, models.DO_NOTHING, db_column='id_responsable', blank=True, null=True)
    correo_sede = models.CharField(max_length=100, blank=True, null=True)
    telefono_sede = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sede'


class Telefonos(models.Model):
    id_telefono = models.AutoField(primary_key=True)
    numero_telefono = models.CharField(unique=True, max_length=20)
    tipo_telefono = models.CharField(max_length=20, blank=True, null=True)
    id_persona = models.OneToOneField(Persona, models.DO_NOTHING, db_column='id_persona')

    class Meta:
        managed = False
        db_table = 'telefonos'


class Trabajador(models.Model):
    id_trabajador = models.AutoField(primary_key=True)
    id_persona = models.OneToOneField(Persona, models.DO_NOTHING, db_column='id_persona')
    id_sede = models.ForeignKey(Sede, models.DO_NOTHING, db_column='id_sede', blank=True, null=True)
    id_cargo = models.ForeignKey(Cargo, models.DO_NOTHING, db_column='id_cargo', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trabajador'


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    id_persona = models.ForeignKey(Persona, models.DO_NOTHING, db_column='id_persona')
    id_rol = models.ForeignKey(Rol, models.DO_NOTHING, db_column='id_rol')
    username = models.CharField(unique=True, max_length=50)
    password_hash = models.CharField(max_length=255)
    estado_usuario = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario'


class UsuarioReporte(models.Model):
    id_reporte = models.AutoField(primary_key=True)
    id_lead = models.ForeignKey(Leads, models.DO_NOTHING, db_column='id_lead')
    usuario_reporte = models.CharField(max_length=100, blank=True, null=True)
    password_reporte = models.CharField(max_length=100, blank=True, null=True)
    plataforma_reporte = models.CharField(max_length=100, blank=True, null=True)
    descripcion_reporte = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'usuario_reporte'