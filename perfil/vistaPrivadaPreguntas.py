from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def PreguntasPrivadas(request, id_usuario):
    return HttpResponseRedirect(reverse('perfil:preguntasprivadaspagina', args=(id_usuario,1)))

def PreguntasPrivadasConIndice(request, id_usuario, pagina):

    if int(pagina) == 0:
        return HttpResponseRedirect(reverse('perfil:preguntasprivadaspagina', args=(id_usuario,1)))



    #comprueba que el usuario exista
    from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_usuario_en_tabla_usuario
    aa = comprueba_exista_usuario_en_tabla_usuario(id_usuario)
    if aa.salir:
        return HttpResponse("Error en sql perfil 1")
    if not aa.existe:
        return HttpResponse("el usuario no existe")

    #cuenta preguntas
    from perfil.BaseDeDatosPreguntas import cuenta_preguntas
    mm = cuenta_preguntas(id_usuario)
    if mm.salir:
        return HttpResponse("Error en sql perfil 1.5")

    numero_maxima_paginas = 0
    if int(mm.numero_preguntas) == 0:
        numero_maxima_paginas = 1
    elif int(mm.numero_preguntas) % 10 == 0:
        numero_maxima_paginas = int(mm.numero_preguntas) / 10
    else:
        numero_maxima_paginas = (int(mm.numero_preguntas)//10) + 1

    if int(pagina) > numero_maxima_paginas:
            return HttpResponseRedirect(reverse('perfil:preguntasprivadaspagina', args=(id_usuario,1)))

    #levanto preguntas
    from perfil.BaseDeDatosPreguntas import levanta_preguntas
    pagina2 = ((int(pagina)*10)-10)
    bb = levanta_preguntas(id_usuario, pagina2)
    if bb.salir:
        return HttpResponse("Error en sql perfil 2")

    from perfil.BaseDeDatosPreguntas import esperoespero
    list_obje1 = []
    for aaa in bb.lista_preguntas:
        list_obje1.append(esperoespero(aaa))

    #levanto datos del usuario
    from BASEdeDATOSglobal.ConsultasGenerales import datos_usuario_mas_direccion_foto
    ee = datos_usuario_mas_direccion_foto(id_usuario)
    if ee.salir:
        return HttpResponse("Error en sql perfil 5")
    from perfil.BaseDeDatosPreguntas import miel4
    list_obje10 = []
    for eee in ee.datos_user:
        list_obje10.append(miel4(eee))




    #levanto grupos

    from BASEdeDATOSglobal.ConsultasGenerales import levanto_grupo
    uy = levanto_grupo(id_usuario)
    if uy.salir:
        return HttpResponse("Error en sql perfil 5.5")

    class miel100():
        grupo = ''
        def __init__(self, mm):
            self.grupo = mm[0]

    list_obje100 = []
    for uyuy in uy.grupo:
        list_obje100.append(miel100(uyuy))




    if (not ('id' in request.COOKIES)) or (request.COOKIES["id"] == 'cookieMala'):

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
        if int(mm.numero_preguntas) <= 10:
            ver_numerador = False

        hay_preguntas = True
        if int(mm.numero_preguntas) == 0:
            hay_preguntas = False


        permiso = False
        usuario = {'idusuario':id_usuario}
        contenido = {'sqlconsu1':list_obje1, 'sqlconsu4':list_obje10, 'var':permiso, 'idusuario':usuario, 'pag0':p1,'pag':p2,'pag2':p3,'ver_numerador':ver_numerador,'hay_preguntas':hay_preguntas,'grupo':list_obje100}
        response3 =  render(request, 'perfil/preguntas.html', contenido)
        return response3

    else:

        #comprovar si la cookie esite en db
        comprobar = request.COOKIES["id"]
        from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_cookie
        ff = comprueba_exista_cookie(comprobar)
        if ff.salir:
            return HttpResponse("Error en sql perfil 6")

        if ff.existe:

            # traeme el usuario de la cookie
            comprobar = request.COOKIES["id"]
            from BASEdeDATOSglobal.ConsultasGenerales import usuario_basado_cookie
            gg = usuario_basado_cookie(comprobar)
            if gg.salir:
                return HttpResponse("Error en sql perfil 7")

            if not gg.usuario == id_usuario:

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
                if int(mm.numero_preguntas) <= 10:
                    ver_numerador = False


                hay_preguntas = True
                if int(mm.numero_preguntas) == 0:
                    hay_preguntas = False



                permiso = False
                usuario = {'idusuario':id_usuario}
                contenido = {'sqlconsu1':list_obje1, 'sqlconsu4':list_obje10, 'var':permiso, 'idusuario':usuario, 'pag0':p1,'pag':p2,'pag2':p3,'ver_numerador':ver_numerador,'hay_preguntas':hay_preguntas,'grupo':list_obje100}
                response3 =  render(request, 'perfil/preguntas.html', contenido)
                return response3
            else:

                #levanto tecnologia
                from perfil.BaseDeDatosPreguntas import levanta_tecnologia_para_cargar_pregunta
                cc = levanta_tecnologia_para_cargar_pregunta(id_usuario)
                if cc.salir:
                    return HttpResponse("Error en sql perfil 3")
                from perfil.BaseDeDatosPreguntas import miel5
                list_obje2 = []
                for ccc in cc.lista_tecnologia:
                    list_obje2.append(miel5(ccc))

                #levanto idiomas
                from perfil.BaseDeDatosPreguntas import levanta_idioma_para_cargar_pregunta
                dd = levanta_idioma_para_cargar_pregunta(id_usuario)
                if dd.salir:
                    return HttpResponse("Error en sql perfil 4")
                from perfil.BaseDeDatosPreguntas import miel6
                list_obje3 = []
                for ddd in dd.lista_idiomas:
                    list_obje3.append(miel6(ddd))

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
                if int(mm.numero_preguntas) <= 10:
                    ver_numerador = False

                hay_preguntas = True
                if int(mm.numero_preguntas) == 0:
                    hay_preguntas = False


                permiso = True
                usuario = {'idusuario':id_usuario}
                contenido = {'sqlconsu1':list_obje1,'sqlconsu2':list_obje2,'sqlconsu3':list_obje3, 'sqlconsu4':list_obje10, 'var':permiso, 'idusuario':usuario, 'pag0':p1,'pag':p2,'pag2':p3,'ver_numerador':ver_numerador,'hay_preguntas':hay_preguntas,'grupo':list_obje100}
                response3 =  render(request, 'perfil/preguntas.html', contenido)
                return response3

        else:
            retorno = HttpResponseRedirect(reverse('perfil:preguntasprivadaspagina',args=(id_usuario,pagina)))
            retorno.set_cookie('id','cookieMala')
            return retorno