from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render

def AceptarUsuarioEnGrupo(request, grupo):

    if request.method == 'POST':


        if (not('id' in request.COOKIES)) or (request.COOKIES['id'] == 'cookieMala'):
            return HttpResponseRedirect(reverse('loging:logingloging'))

        erroreslista = []
        if not request.POST.get('usuario',''):
            erroreslista.append("error")
        if erroreslista:
            return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))


        from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_usuario_en_tabla_usuario
        aa = comprueba_exista_usuario_en_tabla_usuario(request.POST.get('usuario',''))
        if aa.salir:
            return HttpResponse("error en agregando user 2")

        if not aa.existe:
            return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))



        from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_cookie
        bb = comprueba_exista_cookie(request.COOKIES['id'])
        if bb.salir:
            return HttpResponse("error en agregando user 1")
        if not bb.existe:
            retorno = HttpResponseRedirect(reverse('loging:logingloging'))
            retorno.set_cookie('id','cookieMala')
            return retorno

        from BASEdeDATOSglobal.ConsultasGenerales import comprobar_existencia_grupos
        cc = comprobar_existencia_grupos(grupo)
        if cc.salir:
            return HttpResponse("error en agregando user 2")
        if not cc.existe:
            return HttpResponseRedirect(reverse('muro:muromuro', args=(1,)))

        grupo = cc.nombre_grupo


        from BASEdeDATOSglobal.ConsultasGenerales import usuario_basado_cookie
        dd = usuario_basado_cookie(request.COOKIES['id'])
        if dd.salir:
            return HttpResponse("error en agregando user 3")


        from BASEdeDATOSglobal.ConsultasGenerales import pertenesco_grupo_y_nivel
        ee= pertenesco_grupo_y_nivel(dd.usuario,grupo)
        if ee.salir:
            return HttpResponse("error en agregando user 4")



        if  ee.existe and ee.nivel[0] == 3:


            user = request.POST.get('usuario','')
            ff = pertenesco_grupo_y_nivel(user,grupo)
            if ff.salir:
                return HttpResponse("error en agregando user 2")

            if ff.existe and ff.nivel[0] == 1:


                from BASEdeDATOSglobal.ConsultasGenerales import UsuarioPonerPermisoEn2
                gg = UsuarioPonerPermisoEn2(request.POST.get('usuario',''),grupo)
                if gg.salir:
                    return HttpResponse("error en agregando user 4")

                return HttpResponseRedirect(reverse('grup:grupo_autorizados', args=(grupo,)))

            else:
                return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))
        else:
            return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))
    else:
        return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))




def BajarUsuarioEnGrupo(request, grupo):

    if request.method == 'POST':



        if (not('id' in request.COOKIES)) or (request.COOKIES['id'] == 'cookieMala'):
            return HttpResponseRedirect(reverse('loging:logingloging'))

        erroreslista = []
        if not request.POST.get('usuario',''):
            erroreslista.append("error")
        if erroreslista:
            return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))


        from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_usuario_en_tabla_usuario
        aa = comprueba_exista_usuario_en_tabla_usuario(request.POST.get('usuario',''))
        if aa.salir:
            return HttpResponse("error en agregando user 2")

        if not aa.existe:
            return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))


        from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_cookie
        bb = comprueba_exista_cookie(request.COOKIES['id'])
        if bb.salir:
            return HttpResponse("error en agregando user 1")
        if not bb.existe:
            retorno = HttpResponseRedirect(reverse('loging:logingloging'))
            retorno.set_cookie('id','cookieMala')
            return retorno

        from BASEdeDATOSglobal.ConsultasGenerales import comprobar_existencia_grupos
        cc = comprobar_existencia_grupos(grupo)
        if cc.salir:
            return HttpResponse("error en agregando user 2")
        if not cc.existe:
            return HttpResponseRedirect(reverse('muro:muromuro', args=(1,)))

        grupo = cc.nombre_grupo



        from BASEdeDATOSglobal.ConsultasGenerales import usuario_basado_cookie
        dd = usuario_basado_cookie(request.COOKIES['id'])
        if dd.salir:
            return HttpResponse("error en agregando user 3")


        from BASEdeDATOSglobal.ConsultasGenerales import pertenesco_grupo_y_nivel
        ee= pertenesco_grupo_y_nivel(dd.usuario,grupo)
        if ee.salir:
            return HttpResponse("error en agregando user 4")



        if  ee.existe and ee.nivel[0] == 3:


            user = request.POST.get('usuario','')
            ff = pertenesco_grupo_y_nivel(user,grupo)
            if ff.salir:
                return HttpResponse("error en agregando user 2")

            if ff.existe and ff.nivel[0] == 2:


                from BASEdeDATOSglobal.ConsultasGenerales import BajarLogicamenteUsuarioDeGrupo
                gg = BajarLogicamenteUsuarioDeGrupo(request.POST.get('usuario',''),grupo)
                if gg.salir:
                    return HttpResponse("error en agregando user 4")

                return HttpResponseRedirect(reverse('grup:grupo_autorizados', args=(grupo,)))

            else:
                return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))
        else:
            return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))
    else:
        return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))