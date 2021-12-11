from django.shortcuts import render
from apps.productos.models import Producto
from django.views.generic import ListView

def detalle(request):
    contex = {}
    return render(request, "productos/detalle.html", contex)

class ListarAdmin(ListView):
    template_name="productos/admin/listar.html"
    model = Producto