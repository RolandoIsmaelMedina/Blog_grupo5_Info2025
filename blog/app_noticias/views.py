from django.shortcuts import render
from .models import Noticias, Categorias
from django.contrib.auth.models import User

# Create your views here.
#from .models import Noticias (ver acá lo que dió el profe en la clase de consultas con python)

#VISTAS BASADAS EN funciones:
def inicio(request):
    return render(request, "base.html")

def listar_noticias(request):
    noticias = Noticias.objects.all()
    ctx = {
        'noticias':noticias,
        'titulo_pagina': "NOVEDADES"
    }
    return render (request,"app_noticias/listar_noticias.html",ctx)

#VISTAS BASADAS EN clases (VBC: estas son genéricas):
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from django.urls import reverse_lazy

class noticias_list_views(ListView):
    model = Noticias
    template_name = "app_noticias/listar_noticias.html"
    context_object_name = "noticias"

class Noticia_DetailView(DetailView):
    model = Noticias
    template_name = "app_noticias/detalle_noticia.html"

class Noticia_DeleteView(DeleteView):
    model = Noticias
    template_name = "app_noticias/eliminar_noticia.html"
    success_url = reverse_lazy ("listar noticias")

# Ejemplo de vista basada en funciones para eliminar "Categoría" (VBF)
from django.shortcuts import get_object_or_404, redirect
#cuando es "clase se usa el reverse_leze...cuando es funcion se usa 'redirect"
def eliminar_categoria(request, pk):
    categoria = get_object_or_404(Categorias,pk=pk)

    #ahora hay que validar con lo siguiente:
    if request.method == "post":
        categoria.delete()
        return redirect ("listar noticias")
    return render (request, "categorias/eliminar_categoria.html")





