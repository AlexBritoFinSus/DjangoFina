from django.db import models

# Create your models here.
'''
class Usuarios(models.Model):
    iduser = models.AutoField(db_column='idUser', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=80, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    password = models.CharField(max_length=80, blank=True, null=True)
    idrol = models.IntegerField(db_column='idRol', blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    rango_min = models.IntegerField(blank=True, null=True)
    rango_max = models.IntegerField(blank=True, null=True)
    status = models.BooleanField()
    username = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Usuarios'
'''

class Usuarios(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'
