from django.http import HttpResponse, HttpResponseRedirect

from django.core.urlresolvers import reverse

def agregar_user_grupo(request,grupo):

    if request.method == 'POST':

        if (not('id' in request.COOKIES)) or (request.COOKIES['id'] == 'cookieMala'):
            return HttpResponseRedirect(reverse('loging:logingloging'))

        else:

            from BASEdeDATOSglobal.ConsultasGenerales import comprobar_existencia_grupos
            aa = comprobar_existencia_grupos(grupo)
            if aa.salir:
                return HttpResponse("error en agregar usuario a grupo 1")

            if aa.existe:

                grupo = aa.nombre_grupo

                from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_cookie
                usuario_cookie = request.COOKIES["id"]
                bb = comprueba_exista_cookie(usuario_cookie)
                if bb.salir:
                    return HttpResponse("error en agregar usuario a grupo 2")

                if bb.existe:

                    from BASEdeDATOSglobal.ConsultasGenerales import usuario_basado_cookie
                    dd = usuario_basado_cookie(usuario_cookie)
                    if dd.salir:
                        return HttpResponse("error en agregar usuario a grupo 3")

                    from BASEdeDATOSglobal.ConsultasGenerales import pertenesco_grupo_y_nivel
                    cc = pertenesco_grupo_y_nivel(dd.usuario,grupo)
                    if cc.salir:
                        return HttpResponse("error en agregar usuario a grupo 2.5")

                    if cc.existe == False:


                        from BASEdeDATOSglobal.ConsultasGenerales import cargar_en_tabla_permisos_grupos
                        acceso = repr(1)
                        ee = cargar_en_tabla_permisos_grupos(dd.usuario,grupo,acceso)
                        if ee.salir:
                            return HttpResponse("error en agregar usuario a grupo 4")
                        return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))


                    if cc.existe and cc.nivel[0] == 0:

                        from BASEdeDATOSglobal.ConsultasGenerales import usuario_basado_cookie
                        dd = usuario_basado_cookie(usuario_cookie)
                        if dd.salir:
                            return HttpResponse("error en agregar usuario a grupo 3.2")

                        from BASEdeDATOSglobal.ConsultasGenerales import suber_de_cero_a_uno
                        solmar = suber_de_cero_a_uno(dd.usuario,grupo)
                        if solmar.salir:
                            return HttpResponse("error en agregar usuario a grupo 3.3")

                        return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))

                    else:
                        return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))


                # la cookie no esta en db
                else:
                    response = HttpResponseRedirect(reverse('loging:logingloging'))
                    response.set_cookie('id','cookieMala')
                    return response


            else:
                return HttpResponse("El grupo al que te quieres agregar no existe")

    else:
        return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))