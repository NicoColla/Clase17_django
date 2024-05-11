from django.http import HttpResponse
from django.template import Context, Template
from django.shortcuts import render
from datetime import datetime


def saludo(request):
    return HttpResponse("HOLA ._________.")

def segunda_vista(request):
    return HttpResponse("<h1> puedo usar etiquetas html en la respuesta </h1>")

def nombre(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido = apellido.capitalize()
    return HttpResponse(f"<h1>{apellido}, {nombre}</h1>")

#def probando_template(request):
#    mi_html = open("./templates/template1.html", encoding="UTF-8")
#    mi_template = Template(mi_html.read())
#    mi_html.close()
#    mi_contexto = Context({"Saludo": "HOLA TU COLA XD", "Autor": "Lenga"})
#    mi_documento = mi_template.render(mi_contexto)
#    return HttpResponse(mi_documento)

def probando_template(request):
    datos = {"saludo": "HOLA", 
             "autor": "Nicolás Uriel Lenga",
             "date": datetime.now()}
    return render(request, "template1.html", datos)

def mostrar_notas(request):
    notas = (10, 3, 5, 8, 8, 9)
    return render(request, "notas.html", {"notas": notas})