from django.contrib import admin

from applications.lector.models import Lector

from applications.lector.models import Prestamo

# Register your models here.
admin.site.register(Lector)
admin.site.register(Prestamo)