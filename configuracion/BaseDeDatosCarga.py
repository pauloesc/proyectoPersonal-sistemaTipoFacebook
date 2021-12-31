from django.db import connection

#*****************************************************************************
class carga_tecnologia():
    salir = False
    def __init__(self, request, id_usuario):
        cursor = connection.cursor()
        try:
            sql = "INSERT INTO usuario_lenguaje_nivel (user_lenguaje,user_nivel,user_sabe) VALUES ('"+request.POST.get('tecno','')+"','"+request.POST.get('nivel','')+"','"+id_usuario+"')"
            cursor.execute(sql)
        except:
            self.salir = True
        finally:
            cursor.close()
#*****************************************************************************