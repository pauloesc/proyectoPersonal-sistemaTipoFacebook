from FuncionesExtras.preguntasConCodigo import revisador
#**************************************************************************************************
class miel1():
    def __init__(self, mm):
        self.contenido = revisador(mm[0]).contenido
        self.fecha = mm[1]
        self.preguntalenguaje = mm[2]
        self.usuariopregunta = mm[3]
        self.pregunta_titulo = mm[4]
#**************************************************************************************************
class miel2():
    def __init__(self, mm):
        self.contenido = revisador(mm[0]).contenido
        self.fecha = mm[1]
        self.votos = mm[2]
        self.usuariopregunta = mm[3]
        self.foto = mm[4]
#**************************************************************************************************
class miel4():
    def __init__(self, mm):
        self.username = mm[0]
        self.nombre = mm[1]
        self.apellido = mm[2]
        self.foto = mm[3]
#**************************************************************************************************
class podrido():
    def __init__(self, mm):
        self.idpregunta = mm
#**************************************************************************************************

