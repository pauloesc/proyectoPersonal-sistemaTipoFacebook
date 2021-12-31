from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def cargaPreguntaGrupo(request,grupo):

    if (not ('id' in request.COOKIES)) or (request.COOKIES["id"] == 'cookieMala'):
        return HttpResponseRedirect(reverse('loging:logingloging'))

    else:
        from BASEdeDATOSglobal.ConsultasGenerales import comprobar_existencia_grupos
        abb = comprobar_existencia_grupos(grupo)
        if abb.salir:
            return HttpResponse("error en sql carga pregunta grupos 0")

        if abb.existe:

            grupo = abb.nombre_grupo

            if request.method == 'POST':

                datos_faltantes = []

                if not request.POST.get('preguntaGrupo',''):
                    datos_faltantes.append("error")

                if not datos_faltantes:

                    from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_cookie
                    comprobar = request.COOKIES["id"]
                    aa = comprueba_exista_cookie(comprobar)
                    if aa.salir:
                        return HttpResponse("error en sql carga pregunta grupos 1")

                    if aa.existe:

                        #traeme el usuario de la cookkie
                        from BASEdeDATOSglobal.ConsultasGenerales import usuario_basado_cookie
                        comprobar = request.COOKIES["id"]
                        bb = usuario_basado_cookie(comprobar)
                        if bb.salir:
                            return HttpResponse("error en sql carga pregunta grupos 2")


                        from BASEdeDATOSglobal.ConsultasGenerales import pertenesco_grupo_y_nivel
                        cc= pertenesco_grupo_y_nivel(bb.usuario,grupo)

                        if cc.existe and cc.nivel[0] != 0:

                            from BASEdeDATOSglobal.ConsultasGenerales import cargar_pregunta_grupos
                            dd = cargar_pregunta_grupos(request.POST.get('preguntaGrupo',''),bb.usuario,grupo)
                            if dd.salir:
                                return HttpResponse("error en sql carga pregunta grupos 2")

                            return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))


                        else:
                            return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))


                    else:
                        retorno = HttpResponse("a ocurido algo inesperado")
                        retorno.set_cookie('id','cookieMala')
                        return retorno

                else:
                    return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))

            else:
                return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))

        return HttpResponseRedirect(reverse('muro:muromuro', args=(1,)))
