from django.conf.urls import url
from configuracion.views import mostratDatos
from configuracion.eliminarTecnologia import eliminar
from configuracion.cargarTecnologia import cargar
from configuracion.cargarIdiomas import cargarIdioma
from configuracion.EliminarIdioma import eliminarIdioma

urlpatterns = [
                url(r'^(?P<id_usuario>[\w-]+)/configuracion/$',mostratDatos, name='conficonfi'),

                url(r'^(?P<id_usuario>[\w-]+)/bajartecno/$',eliminar, name='confibaja'),

                url(r'^(?P<id_usuario>[\w-]+)/subidatecno/$',cargar, name='confisubida'),

                url(r'^(?P<id_usuario>[\w-]+)/subidaidioma/$',cargarIdioma, name='cargaIdioma'),

                url(r'^(?P<id_usuario>[\w-]+)/eliminaridioma/$',eliminarIdioma, name='eliminarIdioma'),






]