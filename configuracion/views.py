from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def mostratDatos(request, id_usuario):

    if (not ('id' in request.COOKIES)) or (request.COOKIES['id'] == 'cookieMala'):
        return HttpResponseRedirect(reverse('loging:logingloging'))

    else:

        from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_cookie
        comprobar = request.COOKIES["id"]
        aa = comprueba_exista_cookie(comprobar)
        if aa.salir:
            return HttpResponse("Error en sql connfiguracion 1")

        if not aa.existe:
            retorno = HttpResponseRedirect(reverse('loging:logingloging'))
            retorno.set_cookie('id','cookieMala')
            return retorno

        from BASEdeDATOSglobal.ConsultasGenerales import usuario_basado_cookie
        comprobar = request.COOKIES["id"]
        bb = usuario_basado_cookie(comprobar)
        if bb.salir:
            return HttpResponse("Error en sql connfiguracion 2")


        if not (bb.usuario == id_usuario):
            retorno = HttpResponseRedirect(reverse('loging:logingloging'))
            return retorno

        #compruebo que exista el usuario
        from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_usuario_en_tabla_usuario
        cc = comprueba_exista_usuario_en_tabla_usuario(id_usuario)
        if cc.salir:
            return HttpResponse("Error en sql connfiguracion 3")

        if cc.existe:

            #datos del usuario
            from configuracion.BaseDeDatosView import levanta_datos_usuario
            dd =levanta_datos_usuario(id_usuario)
            if dd.salir:
                return HttpResponse("Error en sql connfiguracion 4")

            from configuracion.BaseDeDatosView import miel1
            lista_objetos = []
            for ddd in dd.datos:
                lista_objetos.append(miel1(ddd))

            #levanto idiomas habla usuario
            from configuracion.BaseDeDatosView import levanto_idiomas_habla_usuario
            jj = levanto_idiomas_habla_usuario(id_usuario)
            if jj.salir:
                return HttpResponse("Error en sql connfiguracion 4,5")

            from configuracion.BaseDeDatosView import miel13
            lista_objetos4 = []
            for jjj in jj.datos:
                lista_objetos4.append(miel13(jjj))

            # tecnologias y nivel del usuario
            from configuracion.BaseDeDatosView import levanto_tecnologia_nivel_usuario
            ee = levanto_tecnologia_nivel_usuario(id_usuario)
            if ee.salir:
                return HttpResponse("Error en sql connfiguracion 5")

            lista_objetos2 = []
            from configuracion.BaseDeDatosView import miel2
            for eee in ee.datos:
                lista_objetos2.append(miel2(eee))

            from configuracion.BaseDeDatosView import levanto_lenguajes_db
            ff = levanto_lenguajes_db()
            if ff.salir:
                return HttpResponse("Error en sql connfiguracion 6")

            lista_objetos3 = []
            from configuracion.BaseDeDatosView import miel3
            for fff in ff.datos:
                lista_objetos3.append(miel3(fff))


            from configuracion.BaseDeDatosView import levanto_idiomas_db
            hh = levanto_idiomas_db()
            if hh.salir:
                return HttpResponse("Error en sql connfiguracion 7")

            lista_objetos5 = []
            from configuracion.BaseDeDatosView import miel14
            for hhh in hh.datos:
                lista_objetos5.append(miel14(hhh))


            conx = {'sqlnumero1':lista_objetos, 'sqlnumero2':lista_objetos2, 'sqlnumero3':lista_objetos3, 'sqlnumero4':lista_objetos4,'sqlnumero5':lista_objetos5}
            return render(request, 'configuracion/configura.html', conx)

        else:
            return HttpResponse("el usuario no eeeeexiste")