from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render


def salirmeDeGrupo(request, grupo):

    if not request.method == 'POST':
        return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))


    from BASEdeDATOSglobal.ConsultasGenerales import comprobar_existencia_grupos
    www = comprobar_existencia_grupos(grupo)
    if www.salir:
        return HttpResponse("ERROR SALIRME DE GRUPO 1")


    if not www.existe:
        grupo = www.nombre_grupo
        return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))


    if (not('id' in request.COOKIES)) or (request.COOKIES['id'] == 'cookieMala'):
        return HttpResponseRedirect(reverse('loging:logingloging', args=(1,)))


    grupo = www.nombre_grupo


    from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_cookie
    aa = comprueba_exista_cookie(request.COOKIES['id'])
    if aa.salir:
        return HttpResponse("ERROR SALIRME DE GRUPO 2")
    if not aa.existe:
        retorno = HttpResponseRedirect(reverse('loging:logingloging'))
        retorno.set_cookie('id','cookieMala')
        return retorno


    from BASEdeDATOSglobal.ConsultasGenerales import usuario_basado_cookie
    bb = usuario_basado_cookie(request.COOKIES['id'])
    if bb.salir:
        return HttpResponse("ERROR SALIRME DE GRUPO 3")


    from BASEdeDATOSglobal.ConsultasGenerales import pertenesco_grupo_y_nivel
    cc = pertenesco_grupo_y_nivel(bb.usuario,grupo)
    if cc.salir:
         return HttpResponse("ERROR SALIRME DE GRUPO 4")


    if cc.existe and cc.nivel[0] == 3:
        return HttpResponse('Tu no puedes salirte del grupo debido a que eres administrador del mismo. Si puedes eliminar el grupo.')

    elif cc.existe and cc.nivel[0] != 0:

        from BASEdeDATOSglobal.ConsultasGenerales import BajarLogicamenteUsuarioDeGrupo
        dd = BajarLogicamenteUsuarioDeGrupo(bb.usuario,grupo)
        if dd.salir:
            return HttpResponse("ERROR SALIRME DE GRUPO 5")

        return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))

    else:
        return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))
