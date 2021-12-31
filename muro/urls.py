from django.conf.urls import url
from muro import views

urlpatterns = [ 
                    url(r'^(?P<pagina>[0-9]+)/$', views.muropersonal, name='muromuro'),

                    url(r'^$', views.muropersonalsinindice, name='muromurosinindice'),

]