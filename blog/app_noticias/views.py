from django.shortcuts import render
from .models import Noticias, Categorias
from django.contrib.auth.models import User

# Create your views here.
#from .models import Noticias (ver acá lo que dió el profe en la clase de consultas con python)

#VISTAS BASADAS EN funciones:
def listar_noticias(request):
    noticias = Noticias.objects.all()
    ctx = {
        'noticias':noticias,
        'titulo_pagina': "NOVEDADES"
    }
    return render (request,"app_noticias/listar_noticias.html",ctx)

#VISTAS BASADAS EN clases:

