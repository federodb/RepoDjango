from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola mundo!, Hola coder!")

def muestra_nombre(request, nombre):
    return HttpResponse(f"Buenos dias {nombre}, bienvenido a Coder")


def  prueba_plantilla(request):

    # Se abre el archivo html
    mihtml = open('./DjangoCoder/Templates/index.html')

    # Se crea la plantilla//template
    template = Template(mihtml.read())

    # Se cierra el archivo html
    mihtml.close()

    # Se crea un contexto, se verá más adelante
    contexto = Context()

    # Se renderiza el template dentro de una variable
    documento = template.render(contexto)

    return HttpResponse(documento)