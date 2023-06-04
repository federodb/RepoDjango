from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse
from django.template import Template, Context


def inicio(request):
    return render(request, "AppCoder/inicio.html")

def contacto(request):
    return render(request, "AppCoder/contacto.html")

def rutinas(request):
    return render(request, "AppCoder/rutinas.html")

def iniciosesion(request):
    return render(request, "AppCoder/iniciosesion.html")

def quienessomos(request):
    return render(request, "AppCoder/quienessomos.html")

def crearcuenta(request):
    return render(request, "AppCoder/crearcuenta.html")