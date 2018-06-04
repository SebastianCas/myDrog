from django.db import models
from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.
class Sede(models.Model):

    """ Categorias para clasificar las sedes """
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    def get_absolute_url(self):
        return reverse('sede-list')

class Medicamento(models.Model):

    """ Categorias para clasificar los medicamentos """
    nombre = models.CharField(max_length=50)
    foto = models.ImageField(upload_to='fotos/')

    def __str__(self):
        return self.nombre
    def get_absolute_url(self):
        return reverse('medicamento-list')
    

class Paciente(models.Model):

    """ Categorias para clasificar los pacientes """

    identificacion = models.BigIntegerField(primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    receta = models.CharField(max_length=50)
    medicamento = models.ForeignKey(Medicamento, on_delete='Cascade')
    sede = models.ForeignKey(Sede, on_delete='Cascade')

    def __str__(self):
        return self.nombres
    def get_absolute_url(self):
        return reverse('paciente-list')


@receiver(post_delete, sender=Medicamento)
def photo_delete(sender, instance, **kwargs):
    """ Borra los ficheros de las fotos que se eliminan. """
    instance.foto.delete(False)

def get_absolute_url(self):
    return reverse('medicamento-list')