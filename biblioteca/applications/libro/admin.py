from django.contrib import admin

# Register your models here.
from .models import Categoria, Libro
# Register your models here.

admin.site.register(Libro)
admin.site.register(Categoria)