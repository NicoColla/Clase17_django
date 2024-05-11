from django.http import HttpResponse
from django.template import Context, Template
from django.shortcuts import render
from datetime import datetime


def saludo(request):
    return HttpResponse("HOLA NEGROS")

def segunda_vista(request):
    return HttpResponse("<h1> TE COJO EN LA PISTA JAJAJ XD (puedo usar etiquetas html en la respuesta tu culo con esta jijijijazo) </h1>")

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
    datos = {"saludo": "HOLA TU COLA JAJA XD", 
             "autor": "Nicolás Uriel Lenga",
             "date": datetime.now()}
    return render(request, "template1.html", datos)