from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

class parauno():
    nivel = 0
    def __init__(self, mm):
        self.nivel = mm[0]



def cargaPregunta(request,id_usuario):

    if request.method == 'POST':

        if (not ('id' in request.COOKIES)) or (request.COOKIES["id"] == 'cookieMala'):
            return HttpResponseRedirect(reverse('loging:logingloging'))

        datos_faltantes = []

        if not request.POST.get('titulo',''):
            datos_faltantes.append("La pregunta debe tener un titulo")

        if len(request.POST.get('titulo','')) >= 175:
            datos_faltantes.append("El titulo no puede pasarse de 175 caracteres.")


        if not request.POST.get('idiomamaterno',''):
            datos_faltantes.append("Indique el idioma de la pregunta")
        if not request.POST.get('lenguaje',''):
            datos_faltantes.append("Indique la tecnologia")
        if not request.POST.get('textarea',''):
            datos_faltantes.append("Y la pregunta ??")


        if not datos_faltantes:

            from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_cookie
            comprobar = request.COOKIES["id"]
            aa = comprueba_exista_cookie(comprobar)
            if aa.salir:
                return HttpResponse("error en sql carga pregunta 1")

            if aa.existe:

                #traeme el usuario de la cookkie
                from BASEdeDATOSglobal.ConsultasGenerales import usuario_basado_cookie
                comprobar = request.COOKIES["id"]
                bb = usuario_basado_cookie(comprobar)
                if bb.salir:
                    return HttpResponse("error en sql carga pregunta 2")


                if not (bb.usuario == id_usuario):
                    return HttpResponseRedirect(reverse('perfil:preguntasprivadas', args=(id_usuario,)))


                else:

                    from perfil.BaseDeDatosCargaPregunta import nivel_de_usuario_en_cierta_tecnologia
                    cc= nivel_de_usuario_en_cierta_tecnologia(id_usuario,request)
                    if cc.salir:
                        return HttpResponse("error en sql carga pregunta 2")


                    from perfil.BaseDeDatosCargaPregunta import carga_pregunta
                    dd = carga_pregunta(request,cc.nivel,id_usuario)
                    if dd.salir:
                        return HttpResponse("error en sql carga pregunta 3")

                    return HttpResponseRedirect(reverse('perfil:preguntasprivadas', args=(id_usuario,)))


            else:
                retorno = HttpResponse("a ocurido algo inesperado")
                retorno.set_cookie('id','cookieMala')
                return retorno

        else:
            return HttpResponseRedirect(reverse('perfil:preguntasprivadas', args=(id_usuario,)))

    else:
        return HttpResponse("solo aceptamos post")
