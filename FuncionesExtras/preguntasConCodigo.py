class revisador():
    sDelimitador1 = "<code>"
    sDelimitador2 = "</code>"

    def __init__(self,mm):
        self.contenido = []
        cadena = mm.replace("</code> <code>", "</code><code>")
        # el or en realidad es un and pero como
        # todo esta negado por un not hay que poner un or

        if not (self.sDelimitador1 or self.sDelimitador2) in cadena:
            cadena1 = cadena.replace(self.sDelimitador1, "")
            cadena1 = cadena1.replace(self.sDelimitador2, "")
            cadena1 = cadena1.replace("  "," ")
            #lista = ["texto",cadena1]
            #self.contenido.append(lista)
            self.contenido.append(generadoDefinitivo("texto",cadena1))
            return

        var = 0
        while var < len(cadena):

            if cadena[var:].find(self.sDelimitador1) == 0:
                aa = var + len(self.sDelimitador1)
                bb = var + cadena[var:].find(self.sDelimitador2)
                #lista = ["codigo",cadena[aa:bb]]
                #self.contenido.append(lista)
                self.contenido.append(generadoDefinitivo("codigo",cadena[aa:bb]))
                var += cadena[var:].find(self.sDelimitador2)+len(self.sDelimitador2)

            else:

                if not self.sDelimitador1 in cadena[var:]:
                    cc = len(cadena)
                    #lista = ["texto",cadena[var:cc]]
                    #self.contenido.append(lista)
                    self.contenido.append(generadoDefinitivo("texto",cadena[var:cc]))
                    return

                cc = cadena[var:].find(self.sDelimitador1) + var
                #lista = ["texto",cadena[var:cc]]
                #self.contenido.append(lista)
                self.contenido.append(generadoDefinitivo("texto",cadena[var:cc]))
                var += cadena[var:].find(self.sDelimitador1)


class generadoDefinitivo():
    def __init__(self, que_es, contenido):
        self.que_es = que_es
        self.contenido = contenido