from distutils.command.upload import upload
from django.db import models

# importar departamento para hacer la relacion entre tablas
from applications.departamento.models import Departamento

# Importando libreiras de terceros
from ckeditor.fields import RichTextField

# Create your models here.


class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidad'
        verbose_name_plural = 'Habilidades Empleados'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad


class Empleado(models.Model):
    ''' Modelo para tabla empleado'''

    JOB_CHOICES = (
        ('0', 'CONTADOR'),
        ('1', 'ADMINISTRADOR'),
        ('2', 'ECONOMISTA'),
        ('3', 'OTRO'),
    )
    # Contador
    # Administrador
    # Economista
    # Otro

    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('apellidos', max_length=60)
    full_name = models.CharField(
        'Nombres Completos',
        max_length=120,
        blank=True,
    )
    job = models.CharField('Trabajo', max_length=1, choices=JOB_CHOICES)
    # relacion de 1 a muchos
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    # relacion de muchos a muhcos
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name
