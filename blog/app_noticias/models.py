from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Categorias(models.Model):
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Noticias(models.Model):    
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='noticias') #delete_CASCADE: hace que si se elimina un autor, se eliminará todos los post o comentarios que hizo.
    categoria = models.ForeignKey(Categorias, on_delete=models.SET_NULL, null=True)
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()    
    fecha = models.DateTimeField(default=timezone.now)#esto setea la fecha
    #lo de abajo no se hace pero se da como ejemplo en clase:
    # imagen = models.ImageField(upload_to=imagenes)
    def __str__(self):
        return self.titulo

# REALIZAR COMO TAREA LA CLASE "comentarios"
