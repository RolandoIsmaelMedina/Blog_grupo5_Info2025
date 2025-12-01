from django.contrib import admin
from .models import Noticias, Categorias

# Register your models here.
#admin.site.register(Noticias) #si se quiere usar el decorador @, se elimina la palabra "site"
@admin.register(Noticias)
class NoticiasAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "fecha", "contenido")#esto agrega los campos que pasemos en la tupla
    list_filter = ("titulo",)#esto filtra la noticia por categoría

    search_fields = ("categoria",) #este es un campo de búsqueda según el campo que pasemos en la tupla.

admin.site.register(Categorias)