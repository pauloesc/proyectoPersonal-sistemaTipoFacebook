from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def muropersonalsinindice(request):
    return HttpResponseRedirect(reverse('muro:muromuro', args=(1,)))

def muropersonal(request, pagina):

    if int(pagina) == 0:
        return HttpResponseRedirect(reverse('muro:muromuro', args=(1,)))


    if (not('id' in request.COOKIES)) or (request.COOKIES['id'] == 'cookieMala'):
        return HttpResponseRedirect(reverse('loging:logingloging'))


    from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_cookie
    aa = comprueba_exista_cookie(request.COOKIES["id"])
    if aa.salir:
        return HttpResponse("Error en muro 1")
    if not aa.existe:
        retorno = HttpResponseRedirect(reverse('loging:logingloging'))
        retorno.set_cookie('id','cookieMala')
        return retorno


    from BASEdeDATOSglobal.ConsultasGenerales import usuario_basado_cookie
    bb = usuario_basado_cookie(request.COOKIES["id"])
    if bb.salir:
        return HttpResponse("Error en muro 2")
    usuario = bb.usuario


    from muro.baseDeDatos import cuenta_preguntas_usuario_puede_ver
    cc = cuenta_preguntas_usuario_puede_ver(usuario)
    if cc.salir:
        return HttpResponse("Error en muro 3")

    numero_maxima_paginas = 0
    if int(cc.numero_preguntas) == 0:
        numero_maxima_paginas = 1
    elif int(cc.numero_preguntas) % 10 == 0:
        numero_maxima_paginas = int(cc.numero_preguntas) / 10
    else:
        numero_maxima_paginas = (int(cc.numero_preguntas)//10) + 1

    if int(pagina) > numero_maxima_paginas:
        return HttpResponseRedirect(reverse('muro:muromuro', args=(numero_maxima_paginas,)))


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
    if int(cc.numero_preguntas) <= 10:
        ver_numerador = False

    hay_preguntas = False
    if int(cc.numero_preguntas) == 0:
        hay_preguntas = True


    # toma las preguntas que el usuario puede ver mas con indice de pagina
    from muro.baseDeDatos import preguntas_usuario_puede_ver
    from muro.MIEL import miel
    pagina2 = ((int(pagina)*10)-10)
    dd = preguntas_usuario_puede_ver(bb.usuario,pagina2)
    if dd.salir:
        return HttpResponse("Error en muro 4")

    list_obje = []
    for ddd in dd.lista:
       list_obje.append(miel(ddd))


    #toma datos del usuario
    from BASEdeDATOSglobal.ConsultasGenerales import datos_usuario_mas_direccion_foto
    from muro.MIEL import miel2
    ee = datos_usuario_mas_direccion_foto(bb.usuario)
    if ee.salir:
        return HttpResponse("Error en muro 5")
    list_obje2 = []
    for eee in ee.datos_user:
       list_obje2.append(miel2(eee))


    contenido = {'sqlconsu':list_obje, 'sqlconsu2':list_obje2,'pag0':p1, 'pag':p2,'pag2':p3,'ver_numerador':ver_numerador,'hay_preguntas':hay_preguntas}
    return render(request, 'muro/muro.html', contenido)

