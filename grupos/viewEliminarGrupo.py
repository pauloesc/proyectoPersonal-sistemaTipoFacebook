from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


def eliminarGrupo(request, grupo):

    if request.method == 'POST':

        if (not('id' in request.COOKIES)) or (request.COOKIES['id'] == 'cookieMala'):
            return HttpResponseRedirect(reverse('loging:logingloging'))

        else:
            from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_cookie
            aa = comprueba_exista_cookie(request.COOKIES['id'])
            if aa.salir:
                return HttpResponse("error en eliminar grupo 1")

            if aa.existe:

                from BASEdeDATOSglobal.ConsultasGenerales import comprobar_existencia_grupos
                ab = comprobar_existencia_grupos(grupo)
                if ab.salir:
                    return HttpResponse("error en eliminar grupo 1.2")

                if ab.existe:

                    grupo = ab.nombre_grupo
                    # muy importante

                    from BASEdeDATOSglobal.ConsultasGenerales import usuario_basado_cookie
                    bb = usuario_basado_cookie(request.COOKIES['id'])
                    if bb.salir:
                        return HttpResponse("error en eliminar grupo 2")

                    from BASEdeDATOSglobal.ConsultasGenerales import pertenesco_grupo_y_nivel
                    cc = pertenesco_grupo_y_nivel(bb.usuario,grupo)
                    if cc.salir:
                        return HttpResponse("error en eliminar grupo 3")

                    if cc.existe and cc.nivel[0] == 3:


                        from BASEdeDATOSglobal.ConsultasGenerales import BorrarRespuestaGrupos
                        ddee = BorrarRespuestaGrupos(grupo)
                        if ddee.salir:
                            return HttpResponse("error en eliminar grupo 4")


                        from BASEdeDATOSglobal.ConsultasGenerales import BorrarPreguntasGrupo
                        dd = BorrarPreguntasGrupo(grupo)
                        if dd.salir:
                            return HttpResponse("error en eliminar grupo 4")

                        from BASEdeDATOSglobal.ConsultasGenerales import BorrarPermisosGrupo
                        ee = BorrarPermisosGrupo(grupo)
                        if ee.salir:
                            return HttpResponse("error en eliminar grupo 5")

                        from BASEdeDATOSglobal.ConsultasGenerales import BorrarTablaGrupos
                        ff = BorrarTablaGrupos(grupo)
                        if ff.salir:
                            return HttpResponse("error en eliminar grupo 6")

                        return HttpResponseRedirect(reverse('perfil:preguntasprivadas', args=(bb.usuario,)))

                    else:
                        return HttpResponseRedirect(reverse('perfil:preguntasprivadas', args=(bb.usuario,)))

                else:
                    return HttpResponseRedirect(reverse('muro:muromuro', args=(1,)))


            else:
                    response = HttpResponseRedirect(reverse('loging:logingloging'))
                    response.set_cookie('id','cookieMala')
                    return response

    else:
        return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))