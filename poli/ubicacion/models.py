from django.db import models
from django.urls import reverse

# Create your models here.

class Ubicacion(models.Model):
    id=models.AutoField(primary_key=True)
    codigo=models.CharField(max_length=5)    
    zona=[
        ('V', 'Vip'),
        ('G', 'Gold'),
        ('P', 'Platinium'),
        ('G', 'General')]
    sector=models.CharField(max_length=1, choices=zona, default='V')
    nombre=models.CharField(max_length=30)    
    capacidad=models.PositiveSmallIntegerField()

    def __str__(self):
        txt="{0} ({1}) / Sector: {2}"
        return txt.format(self.nombre, self.codigo, self.sector)

    def get_absolute_url(self):
        return reverse('ubicacion:ubicacion_detail', kwargs={"pk": self.pk})