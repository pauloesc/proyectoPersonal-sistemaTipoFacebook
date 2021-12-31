from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from django.shortcuts import render

def crear(request):

    if request.method == "POST":

        if (not('id' in request.COOKIES)) or (request.COOKIES['id'] == 'cookieMala'):

            return HttpResponseRedirect(reverse('loging:logingloging'))

        else:
            errores = []
            if not request.POST.get('nombregrupo', ''):
                errores.append("nombreFaltante")

            if not request.POST.get('estado', ''):
                errores.append("falta estado")


            if len(request.POST.get('nombregrupo', '')) >= 30:
                errores.append("f")


            if not errores:

                from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_cookie
                usuario = request.COOKIES["id"]
                aa = comprueba_exista_cookie(usuario)
                if aa.salir:
                    return HttpResponse("error en crear grupos 1")

                if aa.existe == True:


                    from ObjetosGenerales.Objetos import filtroUsername
                    zxcv1 = filtroUsername(request.POST.get('nombregrupo', ''))


                    # comprobar que el grupo exista
                    from BASEdeDATOSglobal.ConsultasGenerales import comprobar_existencia_grupos
                    ee = comprobar_existencia_grupos(zxcv1.usuario)
                    if ee.salir:
                        return HttpResponse("error en crear grupos 2")

                    # se figa en la db si el grupo ya existe
                    if not ee.existe:
                    #////

                        from BASEdeDATOSglobal.ConsultasGenerales import crear_grupo
                        # por ahora es publico
                        estado = request.POST.get('estado', '')
                        cc = crear_grupo(zxcv1.usuario,estado)
                        if cc.salir:
                            return HttpResponse("error en crear grupos 3")


                        from BASEdeDATOSglobal.ConsultasGenerales import usuario_basado_cookie
                        comprovar = request.COOKIES["id"]
                        bb = usuario_basado_cookie(comprovar)
                        if bb.salir:
                            return HttpResponse("error en crear grupos 4")

                        from BASEdeDATOSglobal.ConsultasGenerales import cargar_en_tabla_permisos_grupos

                        # el usuario que crea el grupo tiene nivel de acceso 3
                        permiso = repr(3)
                        dd = cargar_en_tabla_permisos_grupos(bb.usuario,zxcv1.usuario,permiso)
                        if dd.salir:
                            return HttpResponse("error en crear grupos 5")

                        return HttpResponseRedirect(reverse('perfil:preguntasprivadas', args=(bb.usuario,)))

                    else:
                        return HttpResponse("el grupo con con nombre: " ""+zxcv1.usuario+"" " ya existe")

                else:
                    retorno = HttpResponseRedirect(reverse('loging:logingloging'))
                    retorno.set_cookie('id','cookieMala')
                    return retorno

            else:
                return HttpResponseRedirect(reverse('muro:muromuro', args=(1,)))

    #from django.shortcuts import render
    #contenido = {}
    #return render(request, 'grupos/creagrupos.html', contenido)
    else:
        return HttpResponseRedirect(reverse('muro:muromuro', args=(1,)))







def vista_grupo(request, nombre_grupo):

    # -----------------------------------------------------------------------
    from BASEdeDATOSglobal.ConsultasGenerales import comprobar_existencia_grupos
    aa = comprobar_existencia_grupos(nombre_grupo)
    if aa.salir:
        return HttpResponse("error en vista grupos 1")
    # -----------------------------------------------------------------------


    if aa.existe:

        # muy importante
        nombre_grupo = aa.nombre_grupo

        if (not('id' in request.COOKIES)) or (request.COOKIES['id'] == 'cookieMala'):

            from BASEdeDATOSglobal.ConsultasGenerales import privacidad_del_grupo
            bb = privacidad_del_grupo(nombre_grupo)
            if bb.salir:
                return HttpResponse("error en vista grupos 2")

            # SI EL GRUPO ES PUBLICO
            if bb.grupo == 'publico':

                from BASEdeDATOSglobal.ConsultasGenerales import levanta_preguntas_grupo
                cc = levanta_preguntas_grupo(nombre_grupo)
                if cc.salir:
                    return HttpResponse("error en vista grupos 2")

                from grupos.generadorObjetosGrupos import preguntas_grupos
                lista_preguntas = []
                for ccc in cc.preguntas:
                    lista_preguntas.append(preguntas_grupos(ccc))

                from BASEdeDATOSglobal.ConsultasGenerales import cuenta_usuarios_grupo
                dd = cuenta_usuarios_grupo(nombre_grupo)
                if dd.salir:
                    return HttpResponse("error en vista grupos 2")

                n_preguntas = dd.cantidad

                mensaje_no_hay_preguntas = False
                if lista_preguntas == []:
                    mensaje_no_hay_preguntas = True

                nombre_grupp = nombre_grupo

                boton_eliminar = False
                boton_unirme = False
                gestion_permiso = False
                hacer_pregunta = False
                registro_y_union = True
                es_privado = False
                preguntas = True

                contexto = {'infopregunta':lista_preguntas,
                            'n_preguntas':n_preguntas,
                            'nombre':nombre_grupp,
                            'boton_eliminar':boton_eliminar,
                            'boton_unirme':boton_unirme,
                            'gestion_permiso':gestion_permiso,
                            'hacer_pregunta':hacer_pregunta,
                            'registro_y_union':registro_y_union,
                            'es_privado':es_privado,
                            'preguntas':preguntas,
                            'mensaje_no_hay_preguntas':mensaje_no_hay_preguntas
                            }
                return render(request,'grupos/grupos.html', contexto)
                # -----------------------------------------------------------------------

            # SI EL GRUPO ES PRIVADO.
            else:

                n_preguntas = 'INDEFINIDO'
                nombre_grupp = nombre_grupo
                boton_eliminar = False
                boton_unirme = False
                gestion_permiso = False
                hacer_pregunta = False
                registro_y_union = True
                es_privado = True
                preguntas = False

                contexto = {'n_preguntas':n_preguntas,
                            'nombre':nombre_grupp,
                            'boton_eliminar':boton_eliminar,
                            'boton_unirme':boton_unirme,
                            'gestion_permiso':gestion_permiso,
                            'hacer_pregunta':hacer_pregunta,
                            'registro_y_union':registro_y_union,
                            'es_privado':es_privado,
                            'preguntas':preguntas
                            }
                return render(request,'grupos/grupos.html', contexto)
                # -----------------------------------------------------------------------


        # USUARIO CON COOKIE
        else:

            from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_cookie
            comprobar = request.COOKIES["id"]
            xaa = comprueba_exista_cookie(comprobar)
            if xaa.salir:
                return HttpResponse('error en vista privada grupos 1')

            # # COMPRUEBA QUE LA COOKIE EXISTA EN DB
            if xaa.existe:

                from BASEdeDATOSglobal.ConsultasGenerales import usuario_basado_cookie
                comprobar = request.COOKIES["id"]
                xbb = usuario_basado_cookie(comprobar)
                if xbb.salir:
                    return HttpResponse('error en vista privada grupos 2')

                from BASEdeDATOSglobal.ConsultasGenerales import pertenesco_grupo_y_nivel
                xcc = pertenesco_grupo_y_nivel(xbb.usuario,nombre_grupo)
                if xcc.salir:
                    return HttpResponse('error en vista privada grupos 3')

                # SI PERTENEZCO AL GRUPO Y MI NIVEL DE ACCESO ES DISTINTO DE CERO
                if xcc.existe and xcc.nivel[0] != 0:

                    if xcc.nivel[0] == 3:

                        from BASEdeDATOSglobal.ConsultasGenerales import levanta_preguntas_grupo
                        cc = levanta_preguntas_grupo(nombre_grupo)
                        if cc.salir:
                            return HttpResponse("error en vista grupos 2")
                        from grupos.generadorObjetosGrupos import preguntas_grupos
                        lista_preguntas = []
                        for ccc in cc.preguntas:
                            lista_preguntas.append(preguntas_grupos(ccc))

                        from BASEdeDATOSglobal.ConsultasGenerales import cuenta_usuarios_grupo
                        dd = cuenta_usuarios_grupo(nombre_grupo)
                        if dd.salir:
                            return HttpResponse("error en vista grupos 2")
                        n_preguntas = dd.cantidad

                        mensaje_no_hay_preguntas = False
                        if lista_preguntas == []:
                            mensaje_no_hay_preguntas = True

                        nombre_grupp = nombre_grupo

                        boton_eliminar = True
                        boton_unirme = False
                        gestion_permiso = True
                        hacer_pregunta = True
                        registro_y_union = False
                        es_privado = False
                        preguntas = True

                        contexto = {'infopregunta':lista_preguntas,
                                    'n_preguntas':n_preguntas,
                                    'nombre':nombre_grupp,
                                    'boton_eliminar':boton_eliminar,
                                    'boton_unirme':boton_unirme,
                                    'gestion_permiso':gestion_permiso,
                                    'hacer_pregunta':hacer_pregunta,
                                    'registro_y_union':registro_y_union,
                                    'es_privado':es_privado,
                                    'preguntas':preguntas,
                                    'mensaje_no_hay_preguntas':mensaje_no_hay_preguntas
                                    }
                        return render(request,'grupos/grupos.html', contexto)
                        # -----------------------------------------------------------------------


                    elif xcc.nivel[0] == 2:

                        from BASEdeDATOSglobal.ConsultasGenerales import levanta_preguntas_grupo
                        cc = levanta_preguntas_grupo(nombre_grupo)
                        if cc.salir:
                            return HttpResponse("error en vista grupos 2")
                        from grupos.generadorObjetosGrupos import preguntas_grupos
                        lista_preguntas = []
                        for ccc in cc.preguntas:
                            lista_preguntas.append(preguntas_grupos(ccc))

                        from BASEdeDATOSglobal.ConsultasGenerales import cuenta_usuarios_grupo
                        dd = cuenta_usuarios_grupo(nombre_grupo)
                        if dd.salir:
                            return HttpResponse("error en vista grupos 2")
                        n_preguntas = dd.cantidad

                        mensaje_no_hay_preguntas = False
                        if lista_preguntas == []:
                            mensaje_no_hay_preguntas = True

                        nombre_grupp = nombre_grupo

                        boton_eliminar = False
                        boton_unirme = False
                        gestion_permiso = False
                        hacer_pregunta = True
                        registro_y_union = False
                        es_privado = False
                        preguntas = True
                        boton_salirme = True

                        contexto = {'infopregunta':lista_preguntas,
                                    'boton_salirme':boton_salirme,
                                    'n_preguntas':n_preguntas,
                                    'nombre':nombre_grupp,
                                    'boton_eliminar':boton_eliminar,
                                    'boton_unirme':boton_unirme,
                                    'gestion_permiso':gestion_permiso,
                                    'hacer_pregunta':hacer_pregunta,
                                    'registro_y_union':registro_y_union,
                                    'es_privado':es_privado,
                                    'preguntas':preguntas,
                                    'mensaje_no_hay_preguntas':mensaje_no_hay_preguntas
                                    }
                        return render(request,'grupos/grupos.html', contexto)
                        # -----------------------------------------------------------------------

                    # xcc.nivel[0] == 1:
                    else:
                        from BASEdeDATOSglobal.ConsultasGenerales import privacidad_del_grupo
                        nnbb = privacidad_del_grupo(nombre_grupo)
                        if nnbb.salir:
                            return HttpResponse("xcc.nivel==1")

                        if nnbb.grupo == 'publico':

                            #-----------------------------------------------------------------------
                            from BASEdeDATOSglobal.ConsultasGenerales import levanta_preguntas_grupo
                            cc = levanta_preguntas_grupo(nombre_grupo)
                            if cc.salir:
                                return HttpResponse("error en vista grupos 2")

                            from grupos.generadorObjetosGrupos import preguntas_grupos
                            lista_preguntas = []
                            for ccc in cc.preguntas:
                                lista_preguntas.append(preguntas_grupos(ccc))
                            # -----------------------------------------------------------------------

                            # -----------------------------------------------------------------------
                            from BASEdeDATOSglobal.ConsultasGenerales import cuenta_usuarios_grupo
                            dd = cuenta_usuarios_grupo(nombre_grupo)
                            if dd.salir:
                                return HttpResponse("error en vista grupos 2")
                            n_preguntas = dd.cantidad
                            # -----------------------------------------------------------------------

                            # -----------------------------------------------------------------------
                            mensaje_no_hay_preguntas = False
                            if lista_preguntas == []:
                                mensaje_no_hay_preguntas = True

                            # -----------------------------------------------------------------------

                            # -----------------------------------------------------------------------
                            nombre_grupp = nombre_grupo
                            # -----------------------------------------------------------------------

                            # -----------------------------------------------------------------------
                            boton_eliminar = False
                            boton_unirme = False
                            gestion_permiso = False
                            hacer_pregunta = False
                            registro_y_union = False
                            es_privado = False
                            preguntas = True
                            pendiente_solicitud = True
                            boton_salirme = True
                            # -----------------------------------------------------------------------

                            # -----------------------------------------------------------------------
                            contexto = {'infopregunta':lista_preguntas,
                                        'boton_salirme':boton_salirme,
                                        'n_preguntas':n_preguntas,
                                        'nombre':nombre_grupp,
                                        'boton_eliminar':boton_eliminar,
                                        'boton_unirme':boton_unirme,
                                        'gestion_permiso':gestion_permiso,
                                        'hacer_pregunta':hacer_pregunta,
                                        'registro_y_union':registro_y_union,
                                        'es_privado':es_privado,
                                        'preguntas':preguntas,
                                        'mensaje_no_hay_preguntas':mensaje_no_hay_preguntas,
                                        'pendiente_solicitud':pendiente_solicitud
                                        }
                            return render(request,'grupos/grupos.html', contexto)
                            # -----------------------------------------------------------------------



                        else:
                            n_preguntas = 'indefinido'
                            nombre_grupp = nombre_grupo
                            boton_eliminar = False
                            boton_unirme = False
                            gestion_permiso = False
                            hacer_pregunta = False
                            registro_y_union = False
                            es_privado = True
                            preguntas = False
                            pendiente_solicitud = True
                            boton_salirme = True

                            contexto = {'n_preguntas':n_preguntas,
                                        'boton_salirme':boton_salirme,
                                        'nombre':nombre_grupp,
                                        'boton_eliminar':boton_eliminar,
                                        'boton_unirme':boton_unirme,
                                        'gestion_permiso':gestion_permiso,
                                        'hacer_pregunta':hacer_pregunta,
                                        'registro_y_union':registro_y_union,
                                        'es_privado':es_privado,
                                        'preguntas':preguntas,
                                        'pendiente_solicitud':pendiente_solicitud
                                        }
                            return render(request,'grupos/grupos.html', contexto)
                            # -----------------------------------------------------------------------


                # USUARIO LOGEADO QUE NO PERTENECE AL GRUPO
                else:
                    # -----------------------------------------------------------------------
                    from BASEdeDATOSglobal.ConsultasGenerales import privacidad_del_grupo
                    vcc = privacidad_del_grupo(nombre_grupo)
                    if vcc.salir:
                        return HttpResponse("error en vista grupos 2")
                    # -----------------------------------------------------------------------

                    # SI EL GRUPO ES PUBLICO
                    if vcc.grupo == 'publico':

                        # -----------------------------------------------------------------------
                        from BASEdeDATOSglobal.ConsultasGenerales import levanta_preguntas_grupo
                        cc = levanta_preguntas_grupo(nombre_grupo)
                        if cc.salir:
                            return HttpResponse("error en vista grupos 2")

                        from grupos.generadorObjetosGrupos import preguntas_grupos
                        lista_preguntas = []
                        for ccc in cc.preguntas:
                            lista_preguntas.append(preguntas_grupos(ccc))
                        # -----------------------------------------------------------------------

                        # -----------------------------------------------------------------------
                        from BASEdeDATOSglobal.ConsultasGenerales import cuenta_usuarios_grupo
                        dd = cuenta_usuarios_grupo(nombre_grupo)
                        if dd.salir:
                            return HttpResponse("error en vista grupos 2")
                        n_preguntas = dd.cantidad
                        # -----------------------------------------------------------------------

                        # -----------------------------------------------------------------------
                        mensaje_no_hay_preguntas = False
                        if lista_preguntas == []:
                            mensaje_no_hay_preguntas = True

                        # -----------------------------------------------------------------------

                        # -----------------------------------------------------------------------
                        nombre_grupp = nombre_grupo
                        # -----------------------------------------------------------------------

                        # -----------------------------------------------------------------------
                        boton_eliminar = False
                        boton_unirme = True
                        gestion_permiso = False
                        hacer_pregunta = False
                        registro_y_union = False
                        es_privado = False
                        preguntas = True
                        # -----------------------------------------------------------------------

                        # -----------------------------------------------------------------------
                        contexto = {'infopregunta':lista_preguntas,
                                    'n_preguntas':n_preguntas,
                                    'nombre':nombre_grupp,
                                    'boton_eliminar':boton_eliminar,
                                    'boton_unirme':boton_unirme,
                                    'gestion_permiso':gestion_permiso,
                                    'hacer_pregunta':hacer_pregunta,
                                    'registro_y_union':registro_y_union,
                                    'es_privado':es_privado,
                                    'preguntas':preguntas,
                                    'mensaje_no_hay_preguntas':mensaje_no_hay_preguntas
                                    }
                        return render(request,'grupos/grupos.html', contexto)
                        # -----------------------------------------------------------------------

                    # USUARIO LEGEADO VIENDO UN GRUPO AL QUE NO PERTENECE Y EL GRUPO ES PRIVADO
                    else:
                        n_preguntas = 'indefinido'
                        nombre_grupp = nombre_grupo

                        boton_eliminar = False
                        boton_unirme = True
                        gestion_permiso = False
                        hacer_pregunta = False
                        registro_y_union = False
                        es_privado = True
                        preguntas = False

                        contexto = {'n_preguntas':n_preguntas,
                                    'nombre':nombre_grupp,
                                    'boton_eliminar':boton_eliminar,
                                    'boton_unirme':boton_unirme,
                                    'gestion_permiso':gestion_permiso,
                                    'hacer_pregunta':hacer_pregunta,
                                    'registro_y_union':registro_y_union,
                                    'es_privado':es_privado,
                                    'preguntas':preguntas
                                    }
                        return render(request,'grupos/grupos.html', contexto)
                        # -----------------------------------------------------------------------


            # -----------------------------------------------------------------------
            else:
                response = HttpResponseRedirect(reverse('loging:logingloging'))
                response.set_cookie('id','cookieMala')
                return response
            # -----------------------------------------------------------------------

    # -----------------------------------------------------------------------
    # ESTE GRUPO NO EXISTE
    else:
        return HttpResponse("este grupo no existe")
    # -----------------------------------------------------------------------

