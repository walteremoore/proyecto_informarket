from django.shortcuts import render
from apps.productos.models import Producto

def inicio(request):
    productos = Producto.objects.all()
    p1 = Producto.objects.get(id=1)
    print("================================")
    print(p1)
    print("================================")
    usuario = {
        "nombre": "Walter",
        "apellido": "Moore"
    }
    contex = {
        "usuario": usuario,
        "productos": productos
    }
    return render(request, "inicio.html", contex)