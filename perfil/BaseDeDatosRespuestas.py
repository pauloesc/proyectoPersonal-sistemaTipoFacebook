from django.db import connection
#********************************************************************************
class levanta_respuestas_basado_id_usuario():
    respuestas = []
    salir = False
    def __init__(self, id_usuario, indice):
        cursor = connection.cursor()
        try:
            sql = "select respuesta_contenido,respuesta_fecha, votos, respuesta_id, respuesta_username, pregunta_titulo FROM tabla_respuesta INNER JOIN tabla_pregunta ON tabla_respuesta.respuesta_id = tabla_pregunta.pregunta_id WHERE respuesta_username = '"+id_usuario+"' order by respuesta_id desc offset '"+repr(indice)+"' limit 10"
            cursor.execute(sql)
            self.respuestas = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
#********************************************************************************
class cuenta_respuestas():
    numero_respuestas = 0
    salir = False
    def __init__(self, id_usuario):
        cursor = connection.cursor()
        try:
            sql = "select count(*) from tabla_respuesta where respuesta_username = '"+id_usuario+"'"
            cursor.execute(sql)
            mmm = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
        aa = mmm[0]
        self.numero_respuestas = repr(aa[0])
#********************************************************************************
from FuncionesExtras.preguntasConCodigo import revisador
class miel():
    def __init__(self, mm):
        self.contenido = revisador(mm[0]).contenido
        self.fecha = mm[1]
        self.votos =mm[2]
        self.respuestaid = mm[3]
        self.usuariorespuesta = mm[4]
        self.pregunta_titulo = mm[5]
#********************************************************************************
class miel4():
    def __init__(self, mm):
        self.username = mm[0]
        self.nombre = mm[1]
        self.apellido = mm[2]
        self.foto = mm[3]
#********************************************************************************
