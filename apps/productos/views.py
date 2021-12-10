from django.shortcuts import render
from apps.productos.models import Producto

def detalle(request):
    contex = {}
    return render(request, "productos/detalle.html", contex)

