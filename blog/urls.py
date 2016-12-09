from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.ListaCreaPost.as_view(), name='post_list'),
    url(r'^(?P<pk>\d+)/$', views.TraeActualizaDestruyePost.as_view(), name='post_detalle'),
]