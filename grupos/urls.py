from django.conf.urls import url
from grupos.views import crear, vista_grupo
from grupos.viewAgregarAGrupo import agregar_user_grupo
from grupos.viweSalirmeDeGrupo import salirmeDeGrupo
from grupos.viewEliminarGrupo import eliminarGrupo
from grupos.CargarPreguntaGrupos import cargaPreguntaGrupo
from grupos.viewRespuestas import vistaRespuestasGrupo
from grupos.viewCargarRespuestaGrupos import cargarRespuestasGrupo
from grupos.viewAutorizados import vistaPermisosUsuarios
from grupos.viewBajarOSubirUsuarioDeGrupo import AceptarUsuarioEnGrupo, BajarUsuarioEnGrupo

urlpatterns = [

url(r'^$',crear, name='creargrupo'),


url(r'^(?P<nombre_grupo>[\w-]+)/$',vista_grupo, name='vista_grupo'),


url(r'^(?P<grupo>[\w-]+)/unirme/$',agregar_user_grupo, name='unirme_grupo'),


url(r'^(?P<grupo>[\w-]+)/salirme/$',salirmeDeGrupo, name='salirme_grupo'),


url(r'^(?P<grupo>[\w-]+)/eliminar/$',eliminarGrupo, name='eliminar_grupo'),


url(r'^(?P<grupo>[\w-]+)/cargapregunta/$',cargaPreguntaGrupo, name='carga_pregunta_grupo'),


url(r'^(?P<grupo>[\w-]+)/respuesta/(?P<idpregunta>[\w-]+)/$',vistaRespuestasGrupo, name='vista_respuesta_grupo'),


url(r'^(?P<grupo>[\w-]+)/respuesta/(?P<idpregunta>[\w-]+)/cargar/$',cargarRespuestasGrupo, name='cargar_respuesta_grupo'),


url(r'^(?P<grupo>[\w-]+)/autorizados/$',vistaPermisosUsuarios, name='grupo_autorizados'),


url(r'^(?P<grupo>[\w-]+)/autorizados/subir/$',AceptarUsuarioEnGrupo, name='grupo_autorizados_subir'),

url(r'^(?P<grupo>[\w-]+)/autorizados/bajar/$',BajarUsuarioEnGrupo, name='grupo_autorizados_bajar'),

]