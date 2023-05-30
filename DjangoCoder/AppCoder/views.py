from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse
from django.template import Template, Context

# Create your views here.
def curso(request, nombre, numero):

    curso = Curso(nombre=nombre, camada=int(numero))
    curso.save()
    doc = f"Curso: {curso.nombre}<br>Camada: {curso.camada}"
    return HttpResponse(doc)

def inicio(request):
    return HttpResponse("Vista Inicio")

def cursos(request):
    return HttpResponse("Vista Cursos")

def profesores(request):
    return HttpResponse("Vista profesores")

def estudiantes(request):
    return HttpResponse("Vista Estudiantes")

def entregables(request):
    return HttpResponse("Vista entregables")

# Renderizamos la template descargada por BootStrap

def bootstrap(request):

    mihtml = open('./AppCoder/templates/AppCoder/index.html')

    template = Template(mihtml.read())

    mihtml.close()

    contexto = Context()

    documento = template.render(contexto)

    return HttpResponse(documento)