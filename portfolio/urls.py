from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.proyecto_list, name="proyectos"),
]