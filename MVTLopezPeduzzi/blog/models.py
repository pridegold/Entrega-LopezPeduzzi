from django.db import models
from django.contrib.auth.models import User

class Placas_de_video(models.Model):
    nombre = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    img = models.ImageField(upload_to="images/", null=True, blank=True)
    def __str__(self):
        return f"Nombre:{self.nombre}, Marca: {self.marca}"

class Fuentes(models.Model):
    Watts = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)

class Perifericos(models.Model):
    tipo = models.CharField(max_length=40)
    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)


class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    imagen = models.ImageField(upload_to="images/", null=True, blank=True)

