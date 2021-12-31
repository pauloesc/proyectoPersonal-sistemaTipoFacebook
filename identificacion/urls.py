from django.conf.urls import url
from identificacion import views

urlpatterns = [ 
                  url(r'^$', views.inicio, name='logingloging'),

]