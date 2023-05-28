from django.http import HttpResponse
from django.template import Template, Context, loader


#------------------------------------------------------------------------------
def saludo(request):
    return HttpResponse("Hola mundo!, Hola coder!")

#------------------------------------------------------------------------------

def muestra_nombre(request, nombre):
    return HttpResponse(f"Buenos dias {nombre}, bienvenido a Coder")

#------------------------------------------------------------------------------

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

#------------------------------------------------------------------------------

def prueba_contexto(request):

    diccionario = {"nombre": "Rene", "apellido": "Aranzaez", "notas": [4,5,6,3,8,10]}

    # Se abre el archivo html
    mihtml = open('index2.html')

    # Se crea la plantilla//template
    template = Template(mihtml.read())

    # Se cierra el archivo html
    mihtml.close()

    # Se crea un contexto, se verá más adelante
    contexto = Context(diccionario)

    # Se renderiza el template dentro de una variable
    documento = template.render(contexto)

    return HttpResponse(documento)

#------------------------------------------------------------------------------

def loaderPrueba(request):
    diccionario = {
        "nombre": "nombre",
        "apellido": "apellido",
        "notas": [4,8,9,10,7,8]
    }

    template = loader.get_template('index2.html')
    documento = template.render(diccionario)

    return HttpResponse(documento)