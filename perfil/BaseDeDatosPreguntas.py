from django.db import connection
#********************************************************************************
class levanta_preguntas():
    preguntas = True
    salir = False
    lista_preguntas = []
    def __init__(self, id_usuario, pagina):
        cursor = connection.cursor()
        try:
            indice = pagina
            sql = "select pregunta_contenido, pregunta_fecha, pregunta_id, pregunta_lenguaje, pregunta_user,pregunta_titulo from tabla_pregunta where pregunta_user = '"+id_usuario+"' order by pregunta_id desc offset '"+repr(indice)+"' limit 10"
            cursor.execute(sql)
            self.lista_preguntas = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
        if self.lista_preguntas == []:
            self.preguntas = False
#*****************************************************************************
class levanta_idioma_para_cargar_pregunta():
    salir = False
    lista_idiomas = []
    def __init__(self, id_usuario):
        cursor = connection.cursor()
        try:
            sql = "select idioma_sabe from idioma_user where habla_id = '"+id_usuario+"'"
            cursor.execute(sql)
            self.lista_idiomas = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
#*****************************************************************************
class levanta_tecnologia_para_cargar_pregunta():
    salir = False
    lista_tecnologia = []
    def __init__(self, id_usuario):
        cursor = connection.cursor()
        try:
            sql = "SELECT user_lenguaje from usuario_lenguaje_nivel where user_sabe  = '"+id_usuario+"'"
            cursor.execute(sql)
            self.lista_tecnologia = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
#*****************************************************************************
class cuenta_preguntas():
    numero_preguntas = 0
    salir = False
    def __init__(self, id_usuario):
        cursor = connection.cursor()
        try:
            sql = "select count(*) from tabla_pregunta where pregunta_user = '"+id_usuario+"'"
            cursor.execute(sql)
            mmm = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
        aa = mmm[0]
        self.numero_preguntas = repr(aa[0])
#*****************************************************************************





class miel1():
    contenido = ''
    fecha = 0
    preguntaid = 0
    preguntalenguaje = ''
    usuariopregunta = ''
    def __init__(self, mm):
        self.contenido = mm[0]
        self.fecha = mm[1]
        self.preguntaid = mm[2]
        self.preguntalenguaje = mm[3]
        self.usuariopregunta = mm[4]
#*****************************************************************************

class miel5():
    lenguaje = ''
    def __init__(self, mm):
        self.lenguaje = mm[0]
#*****************************************************************************

#*****************************************************************************
class miel6():
    idioma = ''
    def __init__(self, mm):
        self.idioma = mm[0]
#*****************************************************************************
class miel4():
    username = ''
    nombre = ''
    apellido = ''
    foto = ''
    def __init__(self, mm):
        self.username = mm[0]
        self.nombre = mm[1]
        self.apellido = mm[2]
        self.foto = mm[3]


#*********************************************************************************
#*********************************************************************************
#*********************************************************************************
#*********************************************************************************
#*********************************************************************************

from FuncionesExtras.preguntasConCodigo import revisador
class esperoespero():

    def __init__(self, mm):
        self.contenido = revisador(mm[0]).contenido
        self.fecha = mm[1]
        self.preguntaid = mm[2]
        self.preguntalenguaje = mm[3]
        self.usuariopregunta = mm[4]
        self.pregunta_titulo = mm[5]






