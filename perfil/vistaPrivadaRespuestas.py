from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse


def RespuestasPrivadasRedireccion(request, id_usuario):

    return HttpResponseRedirect(reverse('perfil:respuestasprivadas2', args=(id_usuario,1)))

def RespuestasPrivadas(request, id_usuario, pagina):

    if int(pagina) == 0:
        return HttpResponseRedirect(reverse('perfil:respuestasprivadas2', args=(id_usuario,1)))

    # comprobar que el usuario exista
    from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_usuario_en_tabla_usuario
    aa = comprueba_exista_usuario_en_tabla_usuario(id_usuario)
    if aa.salir:
        return HttpResponse("Error en respuestas perfil 1")

    if aa.existe:

        # levanta respuestas
        from perfil.BaseDeDatosRespuestas import levanta_respuestas_basado_id_usuario
        from perfil.BaseDeDatosRespuestas import miel
        pagina2 = ((int(pagina)*10)-10)
        bb = levanta_respuestas_basado_id_usuario(id_usuario, pagina2)
        if bb.salir:
            return HttpResponse("Error en respuestas perfil 2")
        list_obje = []
        for bbb in bb.respuestas:
            list_obje.append(miel(bbb))


        #levanto datos del usuario
        from BASEdeDATOSglobal.ConsultasGenerales import datos_usuario_mas_direccion_foto
        from perfil.BaseDeDatosRespuestas import miel4
        cc = datos_usuario_mas_direccion_foto(id_usuario)
        if cc.salir:
            return HttpResponse("Error en respuestas perfil 3")
        list_obje10 = []
        for ccc in cc.datos_user:
            list_obje10.append(miel4(ccc))

        from perfil.BaseDeDatosRespuestas import cuenta_respuestas
        dd = cuenta_respuestas(id_usuario)
        if dd.salir:
            return HttpResponse("Error en respuestas perfil 4")


        numero_maxima_paginas = 0
        if int(dd.numero_respuestas) == 0:
            numero_maxima_paginas = 1
        elif int(dd.numero_respuestas) % 10 == 0:
            numero_maxima_paginas = int(dd.numero_respuestas) / 10
        else:
            numero_maxima_paginas = (int(dd.numero_respuestas)//10) + 1

        if int(pagina) > numero_maxima_paginas:
            return HttpResponseRedirect(reverse('perfil:respuestasprivadas2', args=(id_usuario,1)))

        valor_pag = int(pagina)
        atras = valor_pag-1
        ahora = valor_pag
        adelante = valor_pag+1

        if ahora == 1:
            atras = 1
        if ahora == int(numero_maxima_paginas):
            adelante = ahora

        p1 = {'pag0':atras}
        p2 = {'pag':ahora}
        p3 = {'pag2':adelante}


        ver_numerador = True
        if int(dd.numero_respuestas) <= 10:
            ver_numerador = False

        hay_respuestas = True
        if int(dd.numero_respuestas) == 0:
            hay_respuestas = False



        usuario = {'idusuario':id_usuario}
        cont = {'sqlconsu':list_obje,'sqlconsu2':list_obje10, 'idusuario':usuario,'pag0':p1,'pag':p2,'pag2':p3,'ver_numerador':ver_numerador,'hay_respuestas':hay_respuestas}
        return render(request, 'perfil/respuestas.html', cont)

    else:
        return HttpResponse("el usuario no existe")
