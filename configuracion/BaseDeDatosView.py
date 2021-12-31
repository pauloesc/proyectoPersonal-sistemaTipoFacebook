from django.db import connection
#*****************************************************************************
class levanta_datos_usuario():
    salir = False
    datos = []
    def __init__(self, id_usuario):
        cursor = connection.cursor()
        try:
            sql = "select username, nombre, apellido, correo, docfile from tabla_usuario INNER JOIN registro_document ON registro_document.filename = tabla_usuario.username and tabla_usuario.username = '"+id_usuario+"'"
            cursor.execute(sql)
            self.datos = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
#*****************************************************************************
class miel1():
    username = ''
    nombre = ''
    apellido = ''
    correo = 0
    foto = ''
    def __init__(self, mm):
        self.username = mm[0]
        self.nombre = mm[1]
        self.apellido = mm[2]
        self.correo = mm[3]
        self.foto = mm[4]
#*****************************************************************************
class levanto_tecnologia_nivel_usuario():
    datos = []
    salir = False
    def __init__(self, id_usuario):
        cursor = connection.cursor()
        try:
            sql = "select user_lenguaje, user_nivel, user_sabe from usuario_lenguaje_nivel where user_sabe = '"+id_usuario+"'"
            cursor.execute(sql)
            self.datos = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
#*****************************************************************************
class levanto_lenguajes_db():
    datos = []
    salir = False
    def __init__(self,):
        cursor = connection.cursor()
        try:
            sql = "select lenguaje from tabla_lenguaje"
            cursor.execute(sql)
            self.datos = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
#*****************************************************************************
class miel2():
    tecnologia = ''
    nivel = 0
    username = ''
    def __init__(self, mm):
        self.tecnologia = mm[0]
        self.nivel = mm[1]
        self.username = mm[2]
#*****************************************************************************
class miel3():
    tecnologia = ''
    def __init__(self, mm):
        self.tecnologia = mm[0]
#*****************************************************************************
class levanto_idiomas_habla_usuario():
    datos = []
    salir = False
    def __init__(self,usuario):
        cursor = connection.cursor()
        try:
            sql = "select idioma_sabe from idioma_user where habla_id = '"+usuario+"'"
            cursor.execute(sql)
            self.datos = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
#*****************************************************************************
class miel13():
    idioma = ''
    def __init__(self, mm):
        self.idioma = mm[0]
#*****************************************************************************
class levanto_idiomas_db():
    datos = []
    salir = False
    def __init__(self):
        cursor = connection.cursor()
        try:
            sql = "select idioma from tabla_idioma"
            cursor.execute(sql)
            self.datos = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
#*****************************************************************************
class miel14():
    idioma = ''
    def __init__(self, mm):
        self.idioma = mm[0]