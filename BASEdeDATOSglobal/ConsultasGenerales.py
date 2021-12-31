from django.db import connection

#******************************************************************************
#IDENTIFICACION

class comprobar_usuario_contrasena():
    acceso = False
    salir = False
    def __init__(self,user,pasw):
        cursor = connection.cursor()
        try:
            sql1 = "select username, passw from tabla_usuario where username='"+user+"' and passw='"+pasw+"';"
            cursor.execute(sql1)
            var = cursor.fetchall()
            if var == []:
                self.acceso = False
            else:
                self.acceso = True
        except:
            self.salir = True
        finally:
            cursor.close()
#******************************************************************************
#IDENTIFICACION

class cargar_cookie():
    salir = False
    def __init__(self,verificador,identidad):
        cursor = connection.cursor()
        try:
            sql2 = "insert into cookie_hash (sesion_llave, usuario) values ('"+verificador+"', '"+identidad+"')"
            cursor.execute(sql2)
        except:
            self.salir = True
        finally:
            cursor.close()
#*******************************************************************************
#IDENTIFICACION
#PREGUNTAS
#respuestas
#carga preguntas

class comprueba_exista_cookie():
    existe = True
    salir = False
    def __init__(self, comprobar):
        cursor = connection.cursor()
        try:
            sql = "select sesion_llave from cookie_hash where sesion_llave = '"+comprobar+"'"
            cursor.execute(sql)
            rows = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
        if rows == []:
            self.existe = False
#*****************************************************************************
# registro
# ( perfil,respuestas )
# ( perfil,preguntas )

class comprueba_exista_usuario_en_tabla_usuario():
    existe = True
    salir = False
    def __init__(self, usuario):
        cursor = connection.cursor()
        try:
            sql = "select lower(username) from tabla_usuario where username = lower('"+usuario+"')"


            cursor.execute(sql)
            rows = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
        if rows == []:
            self.existe = False
#******************************************************************************
# registro

class cargar_usuario():
    salir = False
    def __init__(self,username,nombre,apellido,correo,pasw):
        cursor = connection.cursor()
        try:
            sql = "INSERT INTO tabla_usuario (username, nombre, apellido, correo, passw) VALUES ('"+username+"','"+nombre+"','"+apellido+"','"+correo+"','"+pasw+"')"
            cursor.execute(sql)
        except:
            self.salir = True
        finally:
            cursor.close()
#******************************************************************************
# registro

class inserta_usuario_lenguaje_nivel():
    salir = False
    def __init__(self,username,tecnologia,nivel):
        cursor = connection.cursor()
        try:
            sql = "INSERT INTO usuario_lenguaje_nivel (user_lenguaje, user_nivel, user_sabe) VALUES ('"+tecnologia+"', "+repr(nivel)+", '"+username+"')"
            cursor.execute(sql)
        except:
            self.salir = True
        finally:
            cursor.close()
#******************************************************************************
# registro

class inserta_idioma_user():
    salir = False
    def __init__(self,usuario,materno):
        cursor = connection.cursor()
        try:
            sql = "INSERT INTO idioma_user (habla_id, idioma_sabe) VALUES ('"+usuario+"', '"+materno+"')"
            cursor.execute(sql)
        except:
            self.salir = True
        finally:
            cursor.close()
#******************************************************************************
#preguntas
#MURO
#respuestas


class datos_usuario_mas_direccion_foto():
    datos_user = []
    salir = False
    def __init__(self,usuario):
        cursor = connection.cursor()
        try:
            strstr10 = "select username, nombre, apellido, docfile from tabla_usuario INNER JOIN registro_document ON registro_document.filename = tabla_usuario.username and tabla_usuario.username = '"+usuario+"'"
            cursor.execute(strstr10)
            self.datos_user = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
#******************************************************************************
#PREGUNTAS

class levanto_usuario_de_pregunta():
    usuario = []
    salir = False
    def __init__(self,id_pregunta):
        cursor = connection.cursor()
        try:
            sql = "select pregunta_user from tabla_pregunta WHERE pregunta_id = '"+id_pregunta+"'"
            cursor.execute(sql)
            mmm = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
        aa = mmm[0]
        self.usuario = aa[0]
#******************************************************************************
#PREGUNTAS

class levanta_respuestas_basado_en_idpregunta():
    respuestas = []
    salir = False
    def __init__(self,id_pregunta):
        cursor = connection.cursor()
        try:
            strstr0 = "select respuesta_contenido, respuesta_fecha, votos, respuesta_username, docfile from tabla_respuesta INNER JOIN registro_document ON registro_document.filename = tabla_respuesta.respuesta_username and tabla_respuesta.respuesta_id = '"+id_pregunta+"' order by tabla_respuesta.id asc"
            cursor.execute(strstr0)
            self.respuestas = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
#******************************************************************************
#PREGUNTAS

class levanta_pregunta_basandose_en_idpregunta():
    preguntas = []
    salir = False
    existe = True
    def __init__(self,id_pregunta):
        cursor = connection.cursor()
        try:
            strstr0 = "select pregunta_contenido, pregunta_fecha, pregunta_lenguaje, pregunta_user, pregunta_titulo from tabla_pregunta WHERE pregunta_id = '"+id_pregunta+"'"
            cursor.execute(strstr0)
            self.preguntas = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
        if self.preguntas == []:
            self.existe = False
#******************************************************************************
#PREGUNTAS
#muro
#respuestas
#CARGA_PREGUTAS
class usuario_basado_cookie():
    usuario = []
    salir = False
    def __init__(self,sesion):
        cursor = connection.cursor()
        try:
            sql = "select usuario from cookie_hash where sesion_llave = '"+sesion+"'"
            cursor.execute(sql)
            mmm = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
        aa = mmm[0]
        self.usuario = aa[0]
#******************************************************************************
#PREGUNTAS

class cargo_respuesta():
    salir = False
    def __init__(self,textarea,fecha,id_pregunta,usuario):
        cambiado = textarea
        aa = "'"
        bb = '"'
        ambR = cambiado.replace(aa,bb)
        cursor = connection.cursor()
        try:
            sql = "insert into tabla_respuesta (respuesta_contenido, respuesta_fecha, votos, respuesta_id, respuesta_username) values ('"+ambR+"', '"+fecha+"', '0', '"+id_pregunta+"', '"+usuario+"')"
            cursor.execute(sql)
        except:
            self.salir = True
        finally:
            cursor.close()
#******************************************************************************
class comprobar_existencia_grupos():
    existe = True
    salir = False
    def __init__(self,grupo):
        try:
            cursor = connection.cursor()
            sql = "select nombre from grupos where lower(nombre) = lower('"+grupo+"')"
            cursor.execute(sql)
            grupo = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
        if grupo == []:
            self.existe = False
        else:
            grupp = grupo[0]
            self.nombre_grupo = grupp[0]


class crear_grupo():
    salir = False
    def __init__(self,nombreGrupo,estado):

        try:
            cursor = connection.cursor()
            sql = "INSERT INTO grupos (nombre, estado) VALUES ('"+nombreGrupo+"','"+estado+"')"
            cursor.execute(sql)
        except:
            self.salir = True
        finally:
            cursor.close()

class cargar_en_tabla_permisos_grupos():
    salir = False
    def __init__(self,usuario,grupo,acceso):

        try:
            cursor = connection.cursor()
            sql = "INSERT INTO permisos_grupos (usuario, grupo, permiso) VALUES ('"+usuario+"','"+grupo+"','"+acceso+"')"
            cursor.execute(sql)
        except:
            self.salir = True
        finally:
            cursor.close()


class levanto_grupo():
    grupo = []
    salir = False
    def __init__(self,usuario):
        cursor = connection.cursor()
        try:
            strstr0 = "select grupo from permisos_grupos where usuario = '"+usuario+"' and permiso != 0"
            cursor.execute(strstr0)
            self.grupo = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()



class privacidad_del_grupo():
    grupo = ""
    salir = False
    def __init__(self,grupo):
        cursor = connection.cursor()
        try:
            sql = "select estado from grupos where nombre = '"+grupo+"'"
            cursor.execute(sql)
            mmm = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
        aa = mmm[0]
        self.grupo = aa[0]



class levanta_preguntas_grupo():
    preguntas = []
    salir = False
    def __init__(self,grupo):
        cursor = connection.cursor()
        try:
            strstr0 = "select pregunta_contenido,pregunta_fecha,pregunta_id,pregunta_user,grupo_id,docfile from pregunta_grupos INNER JOIN registro_document on registro_document.filename = pregunta_grupos.pregunta_user where grupo_id = '"+grupo+"'"
            cursor.execute(strstr0)
            self.preguntas = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()


class cuenta_usuarios_grupo():
    cantidad = 0
    salir = False
    def __init__(self,grupo):
        cursor = connection.cursor()
        try:
            sql = "select count(usuario) from permisos_grupos where grupo = '"+grupo+"'"
            cursor.execute(sql)
            mmm = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
        aa = mmm[0]
        self.cantidad = aa[0]


class pertenesco_grupo_y_nivel():
    existe = True
    salir = False
    nivel = 0
    def __init__(self,usuario,grupo):
        try:
            cursor = connection.cursor()
            sql = "select permiso from permisos_grupos where usuario = '"+usuario+"' and grupo = '"+grupo+"'"
            cursor.execute(sql)
            grupo = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
        if grupo == []:
            self.existe = False

        if self.existe:
            self.nivel = grupo[0]



class suber_de_cero_a_uno():
    salir = False
    def __init__(self,usuario,grupo):
        try:
            cursor = connection.cursor()
            sql = "UPDATE permisos_grupos SET permiso='1' WHERE grupo='"+grupo+"' and usuario='"+usuario+"'"
            cursor.execute(sql)
        except:
            self.salir = True
        finally:
            cursor.close()


class BajarLogicamenteUsuarioDeGrupo():
    salir = False
    def __init__(self,usuario,grupo):
        try:
            cursor = connection.cursor()
            sql = "UPDATE permisos_grupos SET permiso='0' WHERE grupo='"+grupo+"' and usuario='"+usuario+"'"
            cursor.execute(sql)
        except:
            self.salir = True
        finally:
            cursor.close()


class UsuarioPonerPermisoEn2():
    salir = False
    def __init__(self,usuario,grupo):
        try:
            cursor = connection.cursor()
            sql = "UPDATE permisos_grupos SET permiso='2' WHERE grupo='"+grupo+"' and usuario='"+usuario+"'"
            cursor.execute(sql)
        except:
            self.salir = True
        finally:
            cursor.close()




class BorrarPreguntasGrupo():
    salir = False
    def __init__(self,grupo):
        try:
            cursor = connection.cursor()
            sql = "delete from pregunta_grupos where grupo_id = '"+grupo+"'"
            cursor.execute(sql)
        except:
            self.salir = True
        finally:
            cursor.close()


class BorrarPermisosGrupo():
    salir = False
    def __init__(self,grupo):
        try:
            cursor = connection.cursor()
            sql = "delete from permisos_grupos where grupo = '"+grupo+"'"
            cursor.execute(sql)
        except:
            self.salir = True
        finally:
            cursor.close()


class BorrarTablaGrupos():
    salir = False
    def __init__(self,grupo):
        try:
            cursor = connection.cursor()
            sql = "delete from grupos where nombre = '"+grupo+"'"
            cursor.execute(sql)
        except:
            self.salir = True
        finally:
            cursor.close()


class BorrarRespuestaGrupos():
    salir = False
    def __init__(self,grupo):
        try:
            cursor = connection.cursor()
            sql = "delete from tabla_respuesta_grupo where respuesta_g_grupo = '"+grupo+"'"
            cursor.execute(sql)
        except:
            self.salir = True
        finally:
            cursor.close()




import time
class cargar_pregunta_grupos():
    salir = False
    def __init__(self,contenido,usuario,grupoid):

        try:
            fecha = time.strftime("%Y")
            fecha2 = time.strftime("%d")
            fecha3 = time.strftime("%m")
            barr = "-"
            total = (fecha+barr+fecha3+barr+fecha2)

            aa = "'"
            bb = '"'
            conte = contenido.replace(aa,bb)

            cursor = connection.cursor()
            sql = "INSERT INTO pregunta_grupos (pregunta_contenido,pregunta_fecha,pregunta_user,grupo_id) VALUES ('"+conte+"','"+total+"','"+usuario+"','"+grupoid+"')"
            cursor.execute(sql)
        except:
            self.salir = True
        finally:
            cursor.close()



class comprobar_exista_pregunta_grupo():
    existe = True
    salir = False
    def __init__(self,idpregu,grupo):
        try:
            cursor = connection.cursor()
            sql = "select pregunta_id from pregunta_grupos where pregunta_id = '"+idpregu+"' and grupo_id = '"+grupo+"'"
            cursor.execute(sql)
            grupo = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()
        if grupo == []:
            self.existe = False


class levanto_pregunta_grupo_para_respu():
    salir = False
    def __init__(self,idpregu):
        try:
            cursor = connection.cursor()
            sql = "select pregunta_contenido,pregunta_fecha,pregunta_id,pregunta_user,grupo_id,docfile from pregunta_grupos INNER JOIN registro_document on registro_document.filename = pregunta_grupos.pregunta_user where pregunta_id = '"+idpregu+"'"
            cursor.execute(sql)
            self.pregunta = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()


class levanto_respuesta_grupo_para_respu():
    salir = False
    def __init__(self,idpregu):
        try:
            cursor = connection.cursor()
            sql = "select respuesta_g_contenido,respuesta_g_username,respuesta_g_fecha,respuesta_g_id,docfile from tabla_respuesta_grupo INNER JOIN registro_document on tabla_respuesta_grupo.respuesta_g_username = registro_document.filename where respuesta_g_id = '"+idpregu+"'"
            cursor.execute(sql)
            self.respuestas = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()


class usuario_en_grupo_nivel_2():
    salir = False
    def __init__(self,grupo):
        try:
            cursor = connection.cursor()
            sql = "select usuario, docfile from permisos_grupos inner join registro_document on permisos_grupos.usuario = registro_document.filename  where permiso = '2' and grupo = '"+grupo+"'"
            cursor.execute(sql)
            self.usuarios = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()

class usuario_en_grupo_nivel_1():
    salir = False
    def __init__(self,grupo):
        try:
            cursor = connection.cursor()
            sql = "select usuario, docfile from permisos_grupos inner join registro_document on permisos_grupos.usuario = registro_document.filename  where permiso = '1' and grupo = '"+grupo+"'"
            cursor.execute(sql)
            self.usuarios = cursor.fetchall()
        except:
            self.salir = True
        finally:
            cursor.close()






class cargar_respuesta_grupos():
    salir = False
    def __init__(self,contenido,usuario,preguid,grupo):

        try:
            fecha = time.strftime("%Y")
            fecha2 = time.strftime("%d")
            fecha3 = time.strftime("%m")
            barr = "-"
            total = (fecha+barr+fecha3+barr+fecha2)

            aa = "'"
            bb = '"'
            conte = contenido.replace(aa,bb)

            cursor = connection.cursor()
            sql = "INSERT INTO tabla_respuesta_grupo (respuesta_g_contenido,respuesta_g_username,respuesta_g_fecha,respuesta_g_id,respuesta_g_grupo) VALUES ('"+conte+"','"+usuario+"','"+total+"','"+preguid+"','"+grupo+"')"
            cursor.execute(sql)
        except:
            self.salir = True
        finally:
            cursor.close()
















