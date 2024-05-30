from claseservicio import servicio
class Nodo:
    __servicio: servicio
    __siguiente: object

    def __init__(self,servicio):
        self.__servicio=servicio
        self.__siguiente=None

    def setSiguiente(self,siguiente):
        self.__siguiente=siguiente

    def getDato(self):
        return self.__servicio

    def getSiguiente(self):
        return self.__siguiente