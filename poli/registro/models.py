from django.db import models
from django.urls import reverse
from persona.models import Persona
from evento.models import Evento

# Create your models here.

class Registro(models.Model):
    id=models.AutoField(primary_key=True)
    persona=models.ForeignKey(Persona, null=False, blank=False, on_delete=models.CASCADE)
    evento=models.ForeignKey(Evento, null=False, blank=False, on_delete=models.CASCADE)
    fechaEvento=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        txt="{0} registrad{1} en el evento {2} / Fecha: {3}"
        if self.persona.sexo=="F":
            letraSexo="a"
        else:
            letraSexo="o"
        fecReg=self.fechaEvento.strftime("%A %d/%m/%Y %H:/%M:/%S")
        return txt.format(self.persona.nombreCompleto(), letraSexo, self.evento, fecReg)

    def get_absolute_url(self):
        return reverse('registro:registro_detail', kwargs={"pk": self.pk})