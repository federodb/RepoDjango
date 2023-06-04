from django.contrib import admin
from .models import Curso, Alumnos, Profesor, Entregable

# Register your models here.
admin.site.register(Curso)

admin.site.register(Alumnos)

admin.site.register(Profesor)

admin.site.register(Entregable)