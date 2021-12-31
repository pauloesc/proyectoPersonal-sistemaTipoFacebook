# -*- encoding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import hashlib
import time

def inicio(request):

    if not request.method == 'POST':
        conx = {}
        return render(request, 'identificacion/index.html', conx)


    if (not('id' in request.COOKIES)) or (request.COOKIES['id'] == 'cookieMala'):


        var_errores = False
        var_usuario = False
        var_pass = False

        if not request.POST.get('identidad',''):
            var_usuario = True
            var_errores = True


        if not request.POST.get('passs',''):
            var_pass = True
            var_errores = True

        if var_errores:
            conx = {
                    'var_usuario':var_usuario,
                    'var_pass':var_pass,
                    'identi':request.POST.get('identidad','')
                    }
            return render(request, 'identificacion/index.html', conx)


        from BASEdeDATOSglobal.ConsultasGenerales import comprobar_usuario_contrasena
        aa = comprobar_usuario_contrasena(request.POST.get('identidad',''),request.POST.get('passs',''))
        if aa.salir:
            return HttpResponse("Error en identificacion 1")

        if not aa.acceso:
            var_incorecto = True
            conx = {'var_incorecto':var_incorecto}
            return render(request, 'identificacion/index.html', conx)


        hora = ""+time.strftime("%H%M%S")+""
        cod = "p2k3qh63"
        total = hora+cod
        verificador = (hashlib.md5(total.encode('utf-8')).hexdigest())

        from BASEdeDATOSglobal.ConsultasGenerales import cargar_cookie
        bb = cargar_cookie(verificador,request.POST.get('identidad',''))
        if bb.salir:
            return HttpResponse("Error en identificacion 2")

        response = HttpResponseRedirect(reverse('muro:muromuro', args=(1,)))
        response.set_cookie('id',''+verificador+'')
        return response

    else:

        from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_cookie
        ANTE = comprueba_exista_cookie(request.COOKIES["id"])
        if ANTE.salir:
            return HttpResponse("Error en identificacion 0")

        if not ANTE.existe:
            conx = {}
            retorno = render(request, 'identificacion/index.html', conx)
            retorno.set_cookie('id','cookieMala')
            return retorno

        return HttpResponseRedirect(reverse('muro:muromuro', args=(1,)))