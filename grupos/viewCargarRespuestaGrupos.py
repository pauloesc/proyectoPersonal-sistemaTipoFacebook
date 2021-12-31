from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


def cargarRespuestasGrupo(request, grupo, idpregunta):

    if request.method == 'POST':

        if (not('id' in request.COOKIES)) or (request.COOKIES['id'] == 'cookieMala'):
            return HttpResponseRedirect(reverse('loging:logingloging'))

        #----------comienzo de carga respuesta grupos---------------------------------------

        from BASEdeDATOSglobal.ConsultasGenerales import comprobar_existencia_grupos
        aa = comprobar_existencia_grupos(grupo)
        if aa.salir:
            return HttpResponse("error en respuesta grupo 1")

        if not aa.existe:
            return HttpResponseRedirect(reverse('muro:muromuro', args=(1,)))

        grupo = aa.nombre_grupo

        lista_errores=[]
        if not request.POST.get('respuestaGrupo',''):
            lista_errores.append("error")

        if lista_errores:
            return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))


        from BASEdeDATOSglobal.ConsultasGenerales import comprobar_exista_pregunta_grupo
        bb = comprobar_exista_pregunta_grupo(idpregunta,grupo)
        if bb.salir:
            return HttpResponse("error en respuesta grupo 2")

        if not bb.existe:
            return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))


        from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_cookie
        cc = comprueba_exista_cookie(request.COOKIES['id'])
        if cc.salir:
            return HttpResponse("error en respuesta grupo 1")

        if not cc.existe:
            retorno = HttpResponseRedirect(reverse('loging:logingloging'))
            retorno.set_cookie('id','cookieMala')
            return retorno


        from BASEdeDATOSglobal.ConsultasGenerales import usuario_basado_cookie
        dd = usuario_basado_cookie(request.COOKIES['id'])
        if dd.salir:
            return HttpResponse("error en respuesta grupo 1")

        from BASEdeDATOSglobal.ConsultasGenerales import pertenesco_grupo_y_nivel
        ee = pertenesco_grupo_y_nivel(dd.usuario,grupo)
        if ee.salir:
            return HttpResponse("error en respuesta grupo 1")

        if ee.existe and ee.nivel[0] >= 2:

            from BASEdeDATOSglobal.ConsultasGenerales import cargar_respuesta_grupos
            ff = cargar_respuesta_grupos(request.POST.get('respuestaGrupo',''),dd.usuario,idpregunta,grupo)
            if ff.salir:
                return HttpResponse("error en respuesta grupo 1")

            return HttpResponseRedirect(reverse('grup:vista_respuesta_grupo', args=(grupo,idpregunta)))

        else:
            return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))

    else:

        from BASEdeDATOSglobal.ConsultasGenerales import comprobar_existencia_grupos
        aa = comprobar_existencia_grupos(grupo)
        if aa.salir:
            return HttpResponse("error en respuesta grupo 1")

        if aa.existe:
            grupo = aa.nombre_grupo
            return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))
        else:
            return HttpResponseRedirect(reverse('muro:muromuro', args=(1,)))
