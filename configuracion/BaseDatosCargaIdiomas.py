from django.db import connection
#*****************************************************************************
class carga_idioma_para_usuario():
    salir = False
    def __init__(self,request,id_usuario):
        cursor = connection.cursor()
        try:
            sql = "INSERT INTO idioma_user (habla_id,idioma_sabe) VALUES ('"+id_usuario+"','"+request.POST.get('idiom','')+"')"
            cursor.execute(sql)
        except:
            self.salir = True
        finally:
            cursor.close()
#*****************************************************************************