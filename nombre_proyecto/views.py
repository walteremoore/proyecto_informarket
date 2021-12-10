# from django.shortcuts import render
# from apps.productos.models import Producto
from django.views.generic.base import TemplateView


"""
# Inicio basado en función
def inicio(request):
    contex = {
        "productos": Producto.objects.all()
    }
    return render(request, "inicio.html", contex) 
"""

class Inicio(TemplateView):
    template_name = "inicio.html"

    def get_context_data(self, **kwargs):
        context = super(Inicio, self).get_context_data(**kwargs)
        context["informacion"] = "Estoy pasando cosas" 
        return context
    