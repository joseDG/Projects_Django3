from django.db import models

# Create your models here.


# simpre que creo un modelo debo registrarlo en admin.py
class Prueba(models.Model):
    titulo = models.CharField(max_length=100)
    subtitulo = models.CharField(max_length=50)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.titulo + self.subtitulo
