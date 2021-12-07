from django.shortcuts import render
from apps.productos.models import Producto

def inicio(request):
    productos = Producto.objects.all()

    usuario = {
        "nombre": "Walter",
        "apellido": "Moore"
    }
    contex = {
        "usuario": usuario,
        "productos": productos
    }
    return render(request, "inicio.html", contex)


def login(request):
    return render(request, "login.html")