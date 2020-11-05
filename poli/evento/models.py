from django.db import models
from django.urls import reverse

# Create your models here.

class Evento(models.Model):
    id=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=5)
    nombre=models.CharField(max_length=50)
    tipoevento=[
        ('C', 'Cultural'),
        ('D', 'Diversión'),
        ('E', 'Educativo'),
        ('S', 'Social'),
        ('M', 'Musical'),
        ('D', 'Deportivo'),
        ('O', 'Otro')]
    tipo=models.CharField(max_length=1, choices=tipoevento, default='C')
    duracion=models.PositiveSmallIntegerField(default=120)
    descripcion=models.CharField(max_length=255)

    def __str__(self):
        txt="{0} (Duración: {1} minuto(s))"
        return txt.format(self.nombre, self.duracion)

    def get_absolute_url(self):
        return reverse('evento:evento_detail', kwargs={"pk": self.pk}) 