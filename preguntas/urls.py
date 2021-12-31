from django.conf.urls import url
from preguntas.views import traer_preguntas_respuestas, cargarespuesta

urlpatterns = [

                url(r'^(?P<id_pregunta>[0-9]+)/$',traer_preguntas_respuestas, name='pregupregu'),

                url(r'^(?P<id_pregunta>[0-9]+)/cargar/$',cargarespuesta, name='pregucarga'),
]