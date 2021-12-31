from django.conf.urls import url
from perfil.vistaPrivadaPreguntas import PreguntasPrivadas, PreguntasPrivadasConIndice
from perfil.vistaPrivadaRespuestas import RespuestasPrivadasRedireccion, RespuestasPrivadas
from perfil.CargaPregunta import cargaPregunta


urlpatterns = [
                url(r'^(?P<id_usuario>[\w-]+)/preguntas/$',PreguntasPrivadas, name='preguntasprivadas'),

                url(r'^(?P<id_usuario>[\w-]+)/$',PreguntasPrivadas, name='preguntasprivadas2'),

                url(r'^(?P<id_usuario>[\w-]+)/preguntas/(?P<pagina>[0-9]+)/$',PreguntasPrivadasConIndice, name='preguntasprivadaspagina'),

                url(r'^(?P<id_usuario>[\w-]+)/respuestas/$',RespuestasPrivadasRedireccion, name='respuestasprivadas'),

                url(r'^(?P<id_usuario>[\w-]+)/respuestas/(?P<pagina>[0-9]+)/$',RespuestasPrivadas, name='respuestasprivadas2'),

                url(r'^(?P<id_usuario>[\w-]+)/cargapregunta/$',cargaPregunta, name='accionaccion'),




]