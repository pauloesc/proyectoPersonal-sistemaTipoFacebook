# -*- encoding: utf-8 -*-
class filtroUsername():
    def __init__(self,usuario):
        self.usuario = usuario
        #controla que el usuario no ingrese caracteres no permitidos.
        permitido = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnmñ -0123456789"
        for letra in self.usuario:
            if letra not in permitido:
              self.usuario = self.usuario.replace(letra,"")

        self.usuario = self.usuario.replace(" ","-")

        self.usuario = self.usuario.replace("--","-")

