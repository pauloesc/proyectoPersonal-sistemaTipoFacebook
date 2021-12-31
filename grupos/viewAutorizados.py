from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render



def vistaPermisosUsuarios(request, grupo):

    if (not('id' in request.COOKIES)) or (request.COOKIES['id'] == 'cookieMala'):
        return HttpResponseRedirect(reverse('loging:logingloging'))

    else:

        from BASEdeDATOSglobal.ConsultasGenerales import comprobar_existencia_grupos
        anteA = comprobar_existencia_grupos(grupo)
        if anteA.salir:
            return HttpResponse("error en vista permisos 0")

        if not anteA.existe:
            return HttpResponseRedirect(reverse('muro:muromuro', args=(1,)))

        grupo = anteA.nombre_grupo

        from BASEdeDATOSglobal.ConsultasGenerales import comprueba_exista_cookie
        aa = comprueba_exista_cookie(request.COOKIES['id'])
        if aa.salir:
            return HttpResponse("error en vista permisos 1")

        from BASEdeDATOSglobal.ConsultasGenerales import usuario_basado_cookie
        bb = usuario_basado_cookie(request.COOKIES['id'])
        if bb.salir:
            return HttpResponse("error en vista permisos 2")

        from BASEdeDATOSglobal.ConsultasGenerales import pertenesco_grupo_y_nivel
        cc = pertenesco_grupo_y_nivel(bb.usuario,grupo)

        if cc.existe and cc.nivel[0] == 3:

            class nombre():
                def __init__(self,mm):
                    self.nombre = mm[0]
                    self.foto = mm[1]

            from BASEdeDATOSglobal.ConsultasGenerales import usuario_en_grupo_nivel_2
            dd = usuario_en_grupo_nivel_2(grupo)
            if dd.salir:
                return HttpResponse("error en vista permisos 3")

            UserPermiso_2 = []
            for ddd in dd.usuarios:
                UserPermiso_2.append(nombre(ddd))


            from BASEdeDATOSglobal.ConsultasGenerales import usuario_en_grupo_nivel_1
            ee = usuario_en_grupo_nivel_1(grupo)
            if ee.salir:
                return HttpResponse("error en vista permisos 4")

            UserPermiso_1 = []
            for eee in ee.usuarios:
                UserPermiso_1.append(nombre(eee))

            class nombreGrupo():
                def __init__(self,mm):
                    self.nomGrup = mm

            nomGrup = nombreGrupo(grupo)

            conn = {'nombresPermiso2':UserPermiso_2,
                    'nombresPermiso1':UserPermiso_1,
                    'nomGrup':nomGrup,
                    }

            return render(request,'grupos/permisos.html', conn)


        else:
            return HttpResponseRedirect(reverse('grup:vista_grupo', args=(grupo,)))





