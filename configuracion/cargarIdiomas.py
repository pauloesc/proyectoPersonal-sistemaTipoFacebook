from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def cargarIdioma(request, id_usuario):

    if (not ('id' in request.COOKIES)) or (request.COOKIES['id'] == 'cookieMala'):
        return HttpResponseRedirect(reverse('loging:logingloging'))

    else:

        errores = []

        if not request.POST.get('idiom',''):
            errores.append('Idioma')

        if not errores:

            from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_usuario_en_tabla_usuario
            aa = comprueba_exista_usuario_en_tabla_usuario(id_usuario)
            if aa.salir:
                return HttpResponse("ERROR EN SQL CARGA IDIOMA 1")

            if aa.existe:

                comprobar = request.COOKIES["id"]
                from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_cookie
                aa = comprueba_exista_cookie(comprobar)
                if aa.salir:
                    return HttpResponse("ERROR EN SQL CARGA IDIOMA 2")

                if not aa.existe:
                    retorno = HttpResponseRedirect(reverse('loging:logingloging'))
                    retorno.set_cookie('id','cookieMala')
                    return retorno

                from BASEdeDATOSglobal.ConsultasGenerales import usuario_basado_cookie
                comprobar = request.COOKIES["id"]
                bb = usuario_basado_cookie(comprobar)
                if bb.salir:
                    return HttpResponse("ERROR EN SQL CARGA IDIOMA 3")


                if (bb.usuario == id_usuario):

                    from configuracion.BaseDatosCargaIdiomas import carga_idioma_para_usuario
                    ll = carga_idioma_para_usuario(request, id_usuario)
                    if ll.salir:
                        return HttpResponse("ERROR EN SQL CARGA IDIOMA 4")

                    else:
                        return HttpResponseRedirect(reverse('confi:conficonfi', args=(id_usuario,)))


                else:
                    retorno = HttpResponseRedirect(reverse('muro:muromuro'))
                    return retorno

            else:
                return HttpResponse("este usuario no exite")

        else:
            return HttpResponseRedirect(reverse('confi:conficonfi', args=(id_usuario,)))