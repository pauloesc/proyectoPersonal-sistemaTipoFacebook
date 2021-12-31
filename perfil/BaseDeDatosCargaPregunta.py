from django.db import connection
#*****************************************************************************
class nivel_de_usuario_en_cierta_tecnologia():
    nivel = 0
    salir = False
    def __init__(self,id_usuario,request):
        cursor = connection.cursor()
        try:
            sql = "select user_nivel from usuario_lenguaje_nivel where user_sabe = '"+id_usuario+"' and user_lenguaje = '"+request.POST.get('lenguaje','')+"'"
            cursor.execute(sql)
            mmm = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
        aa = mmm[0]
        self.nivel = repr(aa[0])
#**************************************************************************
import time
class carga_pregunta():
    salir = False
    def __init__(self, request, nivel, id_usuario):
        cambiado = ""+request.POST.get('textarea','')+""
        #repr(cambiado)
        aa = "'"
        bb = '"'
        ambR = cambiado.replace(aa,bb)
        fecha = time.strftime("%Y")
        fecha2 = time.strftime("%d")
        fecha3 = time.strftime("%m")
        barr = "-"
        total = (fecha+barr+fecha3+barr+fecha2)
        cursor = connection.cursor()
        try:
            #sql = "insert into tabla_pregunta (pregunta_contenido, pregunta_fecha, pregunta_idioma, pregunta_lenguaje, pregunta_nivel, pregunta_user) values ('"+request.POST.get('textarea','')+"','"+total+"','"+request.POST.get('idiomamaterno','')+"','"+request.POST.get('lenguaje','')+"','"+nivel+"','"+id_usuario+"')"
            sql = "insert into tabla_pregunta (pregunta_contenido, pregunta_fecha, pregunta_idioma, pregunta_lenguaje, pregunta_nivel, pregunta_user, pregunta_titulo) values ('"+ambR+"','"+total+"','"+request.POST.get('idiomamaterno','')+"','"+request.POST.get('lenguaje','')+"','"+nivel+"','"+id_usuario+"','"+request.POST.get('titulo','')+"')"

            cursor.execute(sql)
        except:
            self.salir = True
        finally:
            cursor.close()
#*****************************************************************************