from django.shortcuts import render
from .models import Proyecto, Categoria

# Create your views here.

def proyecto_list(request):
    proyectos = Proyecto.publicados.all()
    return render(request, 'portfolio/lista_proyectos.html', {'proyectos': proyectos})
