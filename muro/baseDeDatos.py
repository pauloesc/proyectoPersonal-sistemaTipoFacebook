from django.db import connection
#*************************************************************************
class preguntas_usuario_puede_ver():
    lista = []
    salir = False
    def __init__(self,usuario, pagg):
        cursor = connection.cursor()
        try:
            strstr0 = "SELECT pregunta_contenido, pregunta_fecha, pregunta_id, pregunta_lenguaje, pregunta_user, docfile,pregunta_titulo FROM usuario_lenguaje_nivel INNER JOIN tabla_pregunta ON usuario_lenguaje_nivel.user_lenguaje = tabla_pregunta.pregunta_lenguaje and usuario_lenguaje_nivel.user_nivel = tabla_pregunta.pregunta_nivel and usuario_lenguaje_nivel.user_sabe = '"+usuario+"' INNER JOIN idioma_user ON idioma_user.idioma_sabe=tabla_pregunta.pregunta_idioma and idioma_user.habla_id = usuario_lenguaje_nivel.user_sabe INNER JOIN registro_document ON registro_document.filename =  tabla_pregunta.pregunta_user order by pregunta_id desc offset '"+repr(pagg)+"' limit 10"
            cursor.execute(strstr0)
            self.lista = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
#*************************************************************************
class cuenta_preguntas_usuario_puede_ver():
    numero_preguntas = 0
    salir = False
    def __init__(self, id_usuario):
        cursor = connection.cursor()
        try:
            sql = "SELECT count(*) FROM usuario_lenguaje_nivel INNER JOIN tabla_pregunta ON usuario_lenguaje_nivel.user_lenguaje = tabla_pregunta.pregunta_lenguaje and usuario_lenguaje_nivel.user_nivel = tabla_pregunta.pregunta_nivel and usuario_lenguaje_nivel.user_sabe = '"+id_usuario+"' INNER JOIN idioma_user ON idioma_user.idioma_sabe=tabla_pregunta.pregunta_idioma and idioma_user.habla_id = usuario_lenguaje_nivel.user_sabe"
            cursor.execute(sql)
            mmm = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
        aa = mmm[0]
        self.numero_preguntas = repr(aa[0])
#*****************************************************************************