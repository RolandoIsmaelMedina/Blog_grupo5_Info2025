
from django.urls import path
from .import views
from .views import noticias_list_views, inicio, Noticia_DetailView, Noticia_DeleteView

urlpatterns = [
    #url para vista basada en funciones:
    path("", views.inicio, name="inicio"),
    path("noticias/", views.listar_noticias, name="listar noticias"),

    #url para vista basada en clases:
    path("noticias_b/", noticias_list_views.as_view(), name="listar noticias"),
    path("detalle_noticia/<int:pk>", Noticia_DetailView.as_view()),
    path("eliminar_noticia/<int:pk>", Noticia_DeleteView.as_view()),
    
    #url categoria (armada como función)
    path("eliminar_categoria/<int:pk>", views.eliminar_categoria)
    
] 
