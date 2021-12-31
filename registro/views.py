# -*- encoding: utf-8 -*-

from django.shortcuts import render
from registro.models import Document
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def crearUsuario(request):

    errores = False
    username = False
    nombre = False
    apellido = False
    email = False
    cemail = False
    emailcoincidencia = False
    contrasena = False
    ccontrasena = False
    nocoincide = False
    idioma = False
    nivel = False
    tecno = False
    fotofoto = False
    nacionalidad = False
    nombre_user_existe = False

    correo_invalido = False
    contrasenadescalificada = False

    from configuracion.BaseDeDatosView import levanto_lenguajes_db
    ff = levanto_lenguajes_db()
    if ff.salir:
        return HttpResponse("Error en sql registro 10")

    lista_lenguajes = []
    from configuracion.BaseDeDatosView import miel3
    for fff in ff.datos:
        lista_lenguajes.append(miel3(fff))


    if not request.method == "POST":
        conx = {'tecnologias':lista_lenguajes}
        return render(request, 'registro/registro.html', conx)


    if not request.POST.get('username',''):
        username = True
        errores = True

    if not request.POST.get('nombre',''):
        nombre = True
        errores = True

    if not request.POST.get('apellido',''):
        apellido = True
        errores = True

    nacionalidad = False

    if not request.POST.get('email',''):
        email = True
        errores = True

    if not request.POST.get('cemail',''):
        cemail = True
        errores = True

    if not request.POST.get('email','') == request.POST.get('cemail',''):
        emailcoincidencia = True
        errores = True

    if not request.POST.get('contra',''):
        contrasena = True
        errores = True

    if not request.POST.get('ccontra',''):
        ccontrasena = True
        errores = True

    if not request.POST.get('contra','') == request.POST.get('ccontra',''):
        nocoincide = True
        errores = True

    if len(request.POST.get('contra','')) < 8:
        contrasenadescalificada = True
        errores = True

    if len(request.POST.get('contra','')) > 25:
        contrasenadescalificada = True
        errores = True

    if not request.POST.get('materno',''):
        idioma = True
        errores = True

    if not request.POST.get('nivel',''):
        nivel = True
        errores = True

    if not request.POST.get('tecnologia',''):
        tecno = True
        errores = True

    if not request.FILES.get('filename',''):
        fotofoto = True
        errores = True

    if errores:

        conx = {
        'valoruser': request.POST.get('username',''),
        'valornombre': request.POST.get('nombre',''),
        'valorapellido': request.POST.get('apellido',''),
        'valorcorreo':request.POST.get('email',''),
        'valormaterno': request.POST.get('materno',''),
        'valornivel': request.POST.get('nivel',''),

        'tecnologias':lista_lenguajes,

        'contrasenadescalificada':contrasenadescalificada,
        'nombre_user_existe':nombre_user_existe,
        'username':username,
        'nombre':nombre,
        'apellido':apellido,
        'nacionalidad':nacionalidad,
        'email':email,
        'cemail':cemail,
        'emailcoincidencia':emailcoincidencia,
        'contrasena':contrasena,
        'ccontrasena':ccontrasena,
        'nocoincide':nocoincide,
        'idioma':idioma,
        'nivel':nivel,
        'tecno':tecno,
        'fotofoto':fotofoto
        }
        return render(request, 'registro/registro.html', conx)


    posibleUsuario = request.POST.get('username','')
    from ObjetosGenerales.Objetos import filtroUsername
    aa = filtroUsername(posibleUsuario)

    a1 = aa.usuario

    from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_usuario_en_tabla_usuario
    aa = comprueba_exista_usuario_en_tabla_usuario(a1)
    if aa.salir:
        return HttpResponse("error en sql registro 1")

    if aa.existe:

        nombre_user_existe = True
        fotofoto = True

        conx = {
        'valoruser': request.POST.get('username',''),
        'valornombre': request.POST.get('nombre',''),
        'valorapellido': request.POST.get('apellido',''),
        'valorcorreo':request.POST.get('email',''),
        'valormaterno': request.POST.get('materno',''),
        'valornivel': request.POST.get('nivel',''),

        'tecnologias':lista_lenguajes,
        'nombre_user_existe':nombre_user_existe,
        'fotofoto':fotofoto
        }

        return render(request, 'registro/registro.html', conx)

    a2 = request.POST.get('nombre','')
    a3 = request.POST.get('apellido','')
    a4 = request.POST.get('email','')
    a5 =request.POST.get('contra','')


    from BASEdeDATOSglobal.ConsultasGenerales import cargar_usuario
    bb = cargar_usuario(a1,a2,a3,a4,a5)
    if bb.salir:
        return HttpResponse("error en sql registro 2")

    b2 = request.POST.get('tecnologia','')
    b3 = request.POST.get('nivel','')

    from BASEdeDATOSglobal.ConsultasGenerales import inserta_usuario_lenguaje_nivel
    cc = inserta_usuario_lenguaje_nivel(a1,b2,b3)
    if cc.salir:
        return HttpResponse("error en sql registro 3")

    kulio = request.POST.get('materno','')

    from BASEdeDATOSglobal.ConsultasGenerales import inserta_idioma_user
    dd = inserta_idioma_user(a1,kulio)
    if dd.salir:
        return HttpResponse("error en sql registro 4")


    aaa = request.FILES['filename']
    pppp = Document(docfile=aaa, filename=a1)
    pppp.save()

    return HttpResponseRedirect(reverse('loging:logingloging'))





