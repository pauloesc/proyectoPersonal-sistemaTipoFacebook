from django.db import connection
#*****************************************************************************
class eliminar_idioma():
    salir = False
    def __init__(self,request,id_usuario):
        cursor = connection.cursor()
        try:
            sql = "delete from idioma_user where habla_id = '"+id_usuario+"' and idioma_sabe = '"+request.POST.get('idiom','')+"'"
            cursor.execute(sql)
        except:
            self.salir = True
        finally:
            cursor.close()
#*****************************************************************************