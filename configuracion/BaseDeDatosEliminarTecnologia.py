from django.db import connection
#*****************************************************************************
class eliminar_tecnologia():
    salir = False
    def __init__(self,request,id_usuario):
        cursor = connection.cursor()
        try:
            sql = "delete from usuario_lenguaje_nivel where user_sabe = '"+id_usuario+"' and user_lenguaje = '"+request.POST.get('tecno','')+"'"
            cursor.execute(sql)
        except:
            self.salir = True
        finally:
            cursor.close()
#*****************************************************************************