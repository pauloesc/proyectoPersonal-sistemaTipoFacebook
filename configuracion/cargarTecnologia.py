from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def cargar(request, id_usuario):

    if (not ('id' in request.COOKIES)) or (request.COOKIES['id'] == 'cookieMala'):
        return HttpResponseRedirect(reverse('loging:logingloging'))

    else:

        errores = []

        if not request.POST.get('tecno',''):
            errores.append('lenguaje')
        if not request.POST.get('nivel',''):
            errores.append('nivel')

        if not errores:

            from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_usuario_en_tabla_usuario
            aa = comprueba_exista_usuario_en_tabla_usuario(id_usuario)
            if aa.salir:
                return HttpResponse("ERROR EN SQL CARGA 1")

            if aa.existe:

                comprobar = request.COOKIES["id"]
                from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_cookie
                aa = comprueba_exista_cookie(comprobar)
                if aa.salir:
                    return HttpResponse("ERROR EN SQL CARGA 2")

                if not aa.existe:
                    retorno = HttpResponseRedirect(reverse('loging:logingloging'))
                    retorno.set_cookie('id','cookieMala')
                    return retorno

                from BASEdeDATOSglobal.ConsultasGenerales import usuario_basado_cookie
                comprobar = request.COOKIES["id"]
                bb = usuario_basado_cookie(comprobar)
                if bb.salir:
                    return HttpResponse("ERROR EN SQL CARGA 3")


                if (bb.usuario == id_usuario):

                    from configuracion.BaseDeDatosCarga import carga_tecnologia
                    cc = carga_tecnologia(request,id_usuario)
                    if cc.salir:
                        return HttpResponse("ERROR EN SQL CARGA 3")

                    else:
                        return HttpResponseRedirect(reverse('confi:conficonfi', args=(id_usuario,)))


                else:
                    retorno = HttpResponseRedirect(reverse('muro:muromuro'))
                    return retorno

            else:
                return HttpResponse("este usuario no exite")

        else:
            return HttpResponseRedirect(reverse('confi:conficonfi', args=(id_usuario,)))