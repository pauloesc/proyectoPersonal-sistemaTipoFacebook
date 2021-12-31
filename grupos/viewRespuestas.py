from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render



def vistaRespuestasGrupo(request, grupo, idpregunta):

    from BASEdeDATOSglobal.ConsultasGenerales import comprobar_existencia_grupos
    aa = comprobar_existencia_grupos(grupo)
    if aa.salir:
        return HttpResponse("error en respuesta grupo 1")

    if not aa.existe:
        return HttpResponseRedirect(reverse('muro:muromuro', args=(1,)))

    grupo = aa.nombre_grupo

    from BASEdeDATOSglobal.ConsultasGenerales import comprobar_exista_pregunta_grupo
    bb = comprobar_exista_pregunta_grupo(idpregunta,grupo)
    if bb.salir:
        return HttpResponse("error en respuesta grupo 2")

    if not bb.existe:
        return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))


    if (not('id' in request.COOKIES)) or (request.COOKIES['id'] == 'cookieMala'):

        # LEVANTO PREGUNTA
        from BASEdeDATOSglobal.ConsultasGenerales import levanto_pregunta_grupo_para_respu
        ff = levanto_pregunta_grupo_para_respu(idpregunta)
        if ff.salir:
            return HttpResponse("error en respuesta grupo 3")

        pregunta = []
        from grupos.generadorObjetosGrupos import preguntas_grupos
        for fff in ff.pregunta:
            pregunta.append(preguntas_grupos(fff))


        #LEVANTO RESPUESTAS
        from BASEdeDATOSglobal.ConsultasGenerales import levanto_respuesta_grupo_para_respu
        gg = levanto_respuesta_grupo_para_respu(idpregunta)
        if gg.salir:
            return HttpResponse("error en respuesta grupo 4")

        respuesta = []
        from grupos.generadorObjetosGrupos import respuestas_grupo
        for ggg in gg.respuestas:
            respuesta.append(respuestas_grupo(ggg))

        class funciona():
            def __init__(self,gru,idp):
                self.gru = gru
                self.idp = idp

        objj = []
        objj.append(funciona(grupo,idpregunta))


        conn = {
            'pregunta':pregunta,
            'respuesta':respuesta,
            'paradireccion':objj,
            }
        return render(request,'grupos/respu_grupo.html', conn)


    #visitante con cookie

    from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_cookie
    cc = comprueba_exista_cookie(request.COOKIES['id'])
    if cc.salir:
        return HttpResponse("error en respuesta grupo 1")

    if not cc.existe:
        retorno = HttpResponseRedirect(reverse('loging:logingloging'))
        retorno.set_cookie('id','cookieMala')
        return retorno

    from BASEdeDATOSglobal.ConsultasGenerales import usuario_basado_cookie
    a1a = usuario_basado_cookie(request.COOKIES['id'])
    if a1a.salir:
        return HttpResponse("error en respuesta grupo 1")

    from BASEdeDATOSglobal.ConsultasGenerales import pertenesco_grupo_y_nivel
    a2a = pertenesco_grupo_y_nivel(a1a.usuario,grupo)
    if a2a.salir:
        return HttpResponse("error en respuesta grupo 1")

    if a2a.existe and a2a.nivel[0] >= 2:

        # LEVANTO PREGUNTA
        from BASEdeDATOSglobal.ConsultasGenerales import levanto_pregunta_grupo_para_respu
        ff = levanto_pregunta_grupo_para_respu(idpregunta)
        if ff.salir:
            return HttpResponse("error en respuesta grupo 3")

        pregunta = []
        from grupos.generadorObjetosGrupos import preguntas_grupos
        for fff in ff.pregunta:
            pregunta.append(preguntas_grupos(fff))


        #LEVANTO RESPUESTAS
        from BASEdeDATOSglobal.ConsultasGenerales import levanto_respuesta_grupo_para_respu
        gg = levanto_respuesta_grupo_para_respu(idpregunta)
        if gg.salir:
            return HttpResponse("error en respuesta grupo 4")

        respuesta = []
        from grupos.generadorObjetosGrupos import respuestas_grupo
        for ggg in gg.respuestas:
            respuesta.append(respuestas_grupo(ggg))

        class funciona():
            def __init__(self,gru,idp):
                self.gru = gru
                self.idp = idp
        objj = []
        objj.append(funciona(grupo,idpregunta))


        conn = {'pregunta':pregunta,'respuesta':respuesta,'paradireccion':objj}
        return render(request,'grupos/respu_grupo.html', conn)



    from BASEdeDATOSglobal.ConsultasGenerales import privacidad_del_grupo
    ee = privacidad_del_grupo(grupo)
    if ee.salir:
        return HttpResponse("error en respuesta grupo 1")


    if ee.grupo == 'publico':

        # LEVANTO PREGUNTA
        from BASEdeDATOSglobal.ConsultasGenerales import levanto_pregunta_grupo_para_respu
        ff = levanto_pregunta_grupo_para_respu(idpregunta)
        if ff.salir:
            return HttpResponse("error en respuesta grupo 3")

        pregunta = []
        from grupos.generadorObjetosGrupos import preguntas_grupos
        for fff in ff.pregunta:
            pregunta.append(preguntas_grupos(fff))


        #LEVANTO RESPUESTAS
        from BASEdeDATOSglobal.ConsultasGenerales import levanto_respuesta_grupo_para_respu
        gg = levanto_respuesta_grupo_para_respu(idpregunta)
        if gg.salir:
            return HttpResponse("error en respuesta grupo 4")

        respuesta = []
        from grupos.generadorObjetosGrupos import respuestas_grupo
        for ggg in gg.respuestas:
            respuesta.append(respuestas_grupo(ggg))

        class funciona():
            def __init__(self,gru,idp):
                self.gru = gru
                self.idp = idp
        objj = []
        objj.append(funciona(grupo,idpregunta))

        conn = {'pregunta':pregunta,'respuesta':respuesta,'paradireccion':objj}
        return render(request,'grupos/respu_grupo.html', conn)


    else:

        return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))