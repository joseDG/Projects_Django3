from tabnanny import verbose
from django.db import models

# Create your models here.


class Departamento(models.Model):
    # se pone blank=True para que al llenar este campo no sea obligatorio
    # null = True este sirve como no siempre va registrar un valor o puede registrar un valor nulo
    # unique=True permite no repetir los campos con el mismo nombre
    # hacer un valor editable=False permite no mostrar campos a otros usuarios del admin

    name = models.CharField('Nombre', max_length=50)
    shor_name = models.CharField('Nombre Corto', max_length=25, unique=True)

    # Permite cambiar atributos el dashbord de django
    class Meta:
        verbose_name = 'Mi Departamento'
        verbose_name_plural = 'Areas de la empresa'
        ordering = ['-name']
        unique_together = ('name', 'shor_name')

    # django ya crea los id automaticamente.
    # siempre es bueno acudor ala pagian oficial para  tener mas referencia
    # self.name para el nombre completo
    def __str__(self):
        return str(self.id) + '-' + self.shor_name
