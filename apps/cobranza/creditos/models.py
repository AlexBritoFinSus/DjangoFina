from django.db import models
from django.core import checks, exceptions, validators


class Creditos(models.Model):
    referencia = models.CharField(max_length=255, blank=True, null=True)
    montoentregado = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    fechaactivacion = models.DateField(blank=True, null=True)
    credito = models.CharField(max_length=50, blank=True, null=True)
    idproducto = models.IntegerField()
    cliente = models.CharField(max_length=50, blank=True, null=True)
    producto = models.CharField(max_length=255, blank=True, null=True)
    producto_corto = models.CharField(max_length=255, blank=True, null=True)
    saldo = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    montovencido = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    costos_asociados = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    impuesto = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    impuesto_total = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    iopend = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    vence = models.DateField(blank=True, null=True)
    abono = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    diasmora = models.IntegerField(blank=True, null=True)
    interes_total = models.DecimalField(max_digits=20, decimal_places=2, blank=True, null=True)
    cuenta_2001 = models.CharField(max_length=50, blank=True, null=True)
    cuenta_respiro = models.CharField(max_length=50, blank=True, null=True)
    empresa = models.CharField(max_length=2, blank=True, null=True)
    clave = models.CharField(max_length=50, blank=True, null=False, primary_key = True)
    cantidad_creditos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'creditos'

    def _check_primary_key(self):
        if self.primary_key:
            return [
                checks.Error(
                    "AutoFieldNonPrimary must not set primary_key=True. bla bla bla",
                    obj=self,
                    id="fields.E100",
                )
            ]
        else:
            return []

class Gestores(models.Model):
    idusuario = models.CharField(max_length=60, blank=True, null=True)
    credito = models.CharField(max_length=60, blank=True, null=True)
    cliente = models.CharField(max_length=60, blank=True, null=True)
    empresa = models.CharField(max_length=10, blank=True, null=True)
    fecha = models.DateField()
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'gestores'