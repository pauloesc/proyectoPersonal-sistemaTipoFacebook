from django.conf.urls import url
from registro import views

urlpatterns = [ 
                    url(r'^$', views.crearUsuario, name='registroregistro'),


]