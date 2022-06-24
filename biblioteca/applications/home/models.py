from django.db import models

# Create your models here.
class Persona(models.Model):
    """Model definition for Persona."""

    fullname = models.CharField('nombres', max_length=50)
    pais = models.CharField('Pais', max_length=30)
    pasaporte = models.CharField('Pasaporte', max_length=50)
    edad = models.IntegerField() 
    apelativo = models.CharField('Apelativo', max_length=10)
    
    class Meta:
        """Meta definition for Persona."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        db_table = 'persona'

    def __str__(self):
        """Unicode representation of Persona."""
        return self.full_name

    
