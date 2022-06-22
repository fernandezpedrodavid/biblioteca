from django.db import models

#from local apps
from applications.autor.models import Autor

# Create your models here.
from .managers import LibroManager

class Categoria(models.Model):
    nombre = models.CharField( max_length=30)
    
class Libro(models.Model):
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE  
    )  
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField( max_length=50) 
    fecha = models.DateField('Fecha de lanzamiento') 
    portada = models.ImageField(upload_to='portadas', blank=True, null=True)
    visitas = models.PositiveIntegerField()
    
    objects = LibroManager()
    
    def __str__(self):
        return self.titulo
    