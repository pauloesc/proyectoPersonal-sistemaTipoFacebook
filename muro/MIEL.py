class miel2():
    def __init__(self, mm):
        self.username = mm[0]
        self.nombre = mm[1]
        self.apellido = mm[2]
        self.foto = mm[3]

from FuncionesExtras.preguntasConCodigo import revisador
class miel():
    def __init__(self, mm):
        self.pregunta = revisador(mm[0]).contenido
        self.fecha = mm[1]
        self.preguntaid = mm[2]
        self.preguntalenguaje = mm[3]
        self.usuariopregunta = mm[4]
        self.foto = mm[5]
        self.pregunta_titulo =mm[6]