from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def eliminar(request, id_usuario):

    if (not ('id' in request.COOKIES)) or request.COOKIES['id'] == 'cookieMala':
        return HttpResponseRedirect(reverse('loging:logingloging'))

    else:

        from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_usuario_en_tabla_usuario
        aa = comprueba_exista_usuario_en_tabla_usuario(id_usuario)
        if aa.salir:
            return HttpResponse("Error en sql eliminat tecno 1")

        if aa.existe:
            comprobar = request.COOKIES["id"]
            from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_cookie
            bb = comprueba_exista_cookie(comprobar)
            if bb.salir:
                return HttpResponse("Error en sql eliminat tecno 2")

            if bb.existe:

                if not request.POST.get('tecno',''):
                    return HttpResponseRedirect(reverse('confi:conficonfi', args=(id_usuario,)))


                from BASEdeDATOSglobal.ConsultasGenerales import usuario_basado_cookie
                comprobar = request.COOKIES["id"]
                cc = usuario_basado_cookie(comprobar)
                if cc.salir:
                    return HttpResponse("Error en sql eliminat tecno 3")

                if (cc.usuario == id_usuario):

                    from configuracion.BaseDeDatosEliminarTecnologia import eliminar_tecnologia
                    dd = eliminar_tecnologia(request,id_usuario)
                    if dd.salir:
                        return HttpResponse("Error en sql eliminat tecno 4")

                    return HttpResponseRedirect(reverse('confi:conficonfi', args=(id_usuario,)))

                else:
                    return HttpResponseRedirect(reverse('muro:muromuro'))

            else:
                retorno = HttpResponseRedirect(reverse('loging:logingloging'))
                retorno.set_cookie('id','cookieMala')
                return retorno

        else:
            return HttpResponseRedirect(reverse('muro:muromuro'))