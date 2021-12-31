from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import time

def traer_preguntas_respuestas(request, id_pregunta):


    #levanta pregunta y verifica q exista
    from BASEdeDATOSglobal.ConsultasGenerales import levanta_pregunta_basandose_en_idpregunta
    aa = levanta_pregunta_basandose_en_idpregunta(id_pregunta)
    if aa.salir:
        return HttpResponse("Error en preguntas sql 1")
    if not aa.existe:
        return HttpResponse("no exite la pregunta")
    list_obje = []
    from preguntas.MIEL import miel1
    for aaa in aa.preguntas:
       list_obje.append(miel1(aaa))


    #levanta respuesta
    from BASEdeDATOSglobal.ConsultasGenerales import levanta_respuestas_basado_en_idpregunta
    bb = levanta_respuestas_basado_en_idpregunta(id_pregunta)
    if bb.salir:
        return HttpResponse("Error en preguntas sql 1")
    list_obje2 = []
    from preguntas.MIEL import miel2
    for bbb in bb.respuestas:
       list_obje2.append(miel2(bbb))


    #tomo username para =>>> levanto datos del usuario
    from BASEdeDATOSglobal.ConsultasGenerales import levanto_usuario_de_pregunta
    cc = levanto_usuario_de_pregunta(id_pregunta)
    if cc.salir:
        return HttpResponse("Error en preguntas sql 2")


    from BASEdeDATOSglobal.ConsultasGenerales import datos_usuario_mas_direccion_foto
    dd = datos_usuario_mas_direccion_foto(cc.usuario)
    if dd.salir:
        return HttpResponse("Error en preguntas sql 3")
    list_obje4 = []
    from preguntas.MIEL import miel4
    for ddd in dd.datos_user:
       list_obje4.append(miel4(ddd))


    # si la cookie no tiene id es como un usuario publico
    if (not ('id' in request.COOKIES)) or (request.COOKIES["id"] == 'cookieMala'):

        acceso = False
        contenido = {'sqlconsu':list_obje, 'sqlconsu2':list_obje2,'sqlconsu3':list_obje4, 'acceso':acceso}
        return render(request, 'preguntas/preguntas_y_respuestas.html', contenido)

    else:

        #comprovar si la cookie esite en db
        from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_cookie
        comprobar = request.COOKIES["id"]
        ee = comprueba_exista_cookie(comprobar)
        if ee.salir:
            return HttpResponse("Error en preguntas sql 3")

        if ee.existe:
            from preguntas.MIEL import podrido
            fgf = podrido(id_pregunta)
            acceso = True
            contenido = {'sqlconsu':list_obje, 'sqlconsu2':list_obje2,'sqlconsu3':list_obje4, 'acceso':acceso, 'idpregu':fgf}
            return render(request, 'preguntas/preguntas_y_respuestas.html', contenido)

        else:
            return HttpResponse("no existe esta cookie")




def cargarespuesta(request, id_pregunta):

    if request.method == 'POST':

        if not request.POST.get('textarea',''):
            return HttpResponse("te faltan datos")

        if (not ('id' in request.COOKIES)) or (request.COOKIES["id"] == 'cookieMala'):
            return HttpResponseRedirect(reverse('loging:logingloging'))


        from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_cookie
        usuario = request.COOKIES["id"]
        aa = comprueba_exista_cookie(usuario)
        if aa.salir:
            return HttpResponse("Error en preguntas carga sql 1")
        if not aa.existe:
            return HttpResponse("no exite la cookie para este usuario")

        from BASEdeDATOSglobal.ConsultasGenerales import usuario_basado_cookie
        usuario = request.COOKIES["id"]
        bb = usuario_basado_cookie(usuario)
        if bb.salir:
            return HttpResponse("Error en preguntas carga sql 2")


        fecha = time.strftime("%Y")
        fecha2 = time.strftime("%d")
        fecha3 = time.strftime("%m")
        barr = "-"
        total = (fecha+barr+fecha3+barr+fecha2)

        from BASEdeDATOSglobal.ConsultasGenerales import cargo_respuesta
        cc = cargo_respuesta(request.POST.get('textarea',''), total, id_pregunta, bb.usuario)
        if cc.salir:
            return HttpResponse("Error en preguntas carga sql 3")

        return HttpResponseRedirect(reverse('pregu:pregupregu', args=(id_pregunta,)))


    else:
        return HttpResponseRedirect(reverse('pregu:pregupregu', args=(id_pregunta,)))
