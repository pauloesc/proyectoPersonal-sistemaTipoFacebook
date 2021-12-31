from FuncionesExtras.preguntasConCodigo import revisador

class preguntas_grupos():
    def __init__(self, mm):
        self.contenido = revisador(mm[0]).contenido
        self.fecha = mm[1]
        self.preguntaid = mm[2]
        self.usuario = mm[3]
        self.grupo = mm[4]
        self.foto = mm[5]


class respuestas_grupo():
    def __init__(self, mm):
        self.contenido = revisador(mm[0]).contenido
        self.usuario = mm[1]
        self.fecha = mm[2]
        self.id = mm[3]
        self.foto = mm[4]