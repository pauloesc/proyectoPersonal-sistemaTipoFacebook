from django.conf.urls import include, url
from Gea import settings


urlpatterns = [

                url(r'^inicio/', include('muro.urls', namespace='muro')),

                url(r'^login/', include('identificacion.urls', namespace='loging')),

                url(r'^registro/', include('registro.urls', namespace='registro')),

                url(r'^perfil/', include('perfil.urls', namespace='perfil')),

                url(r'^preguntas/', include('preguntas.urls', namespace='pregu')),

                url(r'^confi/', include('configuracion.urls', namespace='confi')),

                url(r'^grupos/', include('grupos.urls', namespace='grup')),

                url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}, name="imagenes"),
]


