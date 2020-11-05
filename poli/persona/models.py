from django.db import models
from evento.models import Evento

# Create your models here.

class Persona(models.Model):
    numIdentificacion=models.CharField(max_length=20, primary_key=True)
    tipos=[
        ('C', 'Cédula de Ciudadanía'),
        ('E', 'Cédula de Extranjería'),
        ('P', 'Pasaporte'),
        ('O', 'Otro')]
    tipoIdentificacion=models.CharField(max_length=1, choices=tipos, default='C')
    apellidoPaterno=models.CharField(max_length=35)
    apellidoMaterno=models.CharField(max_length=35)
    nombres=models.CharField(max_length=50)
    fechaNacimiento=models.DateField()
    sexos=[
        ('F', 'Femenino'),
        ('M', 'Masculino'),
        ('X', 'Otro')]
    sexo=models.CharField(max_length=1, choices=sexos, default='M')
    telefono=models.CharField(max_length=15)
    direccion=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    evento=models.ForeignKey(Evento, null=False, blank=False, on_delete=models.CASCADE)

    def nombreCompleto(self):
        txt="{0} {1}, {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

    def __str__(self):
        txt="{0} / Evento: {1}"
        return txt.format(self.nombreCompleto(), self.evento)