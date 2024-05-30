import csv
from clasenodo import Nodo
from claseembalaje import embalaje
from clasetransporte import transporte

class lista:
    __comienzo:Nodo
    __actual:Nodo
    __indice:int
    __tope:int

    def __init__(self):
        self.__comienzo=None
        self.__actual=None
        self.__indice=0
        self.__tope=0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato= self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
    def getTope(self):
        return self.__tope
    
    def agregarservicio(self,servicio):
        nodo= Nodo(servicio)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        self.__tope+=1

    def carga(self):
        
        archivo=open("transporte.csv","r")
        reader=csv.reader(archivo,delimiter=';')
        for fila in reader:
                try:
                    print(f"Transporte fila: {fila}")
                    nuevotransporte = transporte(fila[0], fila[1], fila[2], fila[3], int(fila[4]), float(fila[5]), int(fila[6]), fila[7])
                    self.agregarservicio(nuevotransporte)
                except IndexError as e:
                    print(f"Error de índice en la fila: {fila}, error: {e}")
                except ValueError as e:
                    print(f"Error de valor en la fila: {fila}, error: {e}")
        archivo.close()
        archivo=open("embalaje.csv","r")
        reader1=csv.reader(archivo,delimiter=';')
        for fila1 in reader1:
                try:
                    nuevoembalaje = embalaje(fila1[0], fila1[1], fila1[2], fila1[3], int(fila1[4]), int(fila1[5]), int(fila1[6]), int(fila1[7]))
                    self.agregarservicio(nuevoembalaje)
                except IndexError as e:
                    print(f"Error de índice en la fila: {fila1}, error: {e}")
                except ValueError as e:
                    print(f"Error de valor en la fila: {fila1}, error: {e}")
        archivo.close()
    def mostar(self):
        for servi in self:
            print(servi)
    
    def mostar_servicio_transporte(self):
        aux=self.__comienzo
        while aux is not None:
            if isinstance(aux.getDato(),transporte):
                print(f"""Servicio de Transporte realizado
                            Contratante:               Costo total:
                            {aux.getDato().get_nombre_contratante()}        {aux.getDato().get_coste_total()} """
                                )
            aux=aux.getSiguiente()
    
    def paquetes_50_kilos(self):
        aux=self.__comienzo
        while aux is not None:
            if isinstance(aux.getDato(),embalaje):
                print(f"Paquetes mayores a 50KG: {aux.getDato().get_paquete_mayor_a_50()}")
            else:
                print("no hay paquetes que superen los 50 KG")
            aux=aux.getSiguiente()
    
    def servicio_con_mas_contrataciones(self,fecha):
        contador = 0
        contador1 = 0
        aux = self.__comienzo
        while aux is not None:
            if isinstance(aux.getDato(), transporte) and aux.getDato().get_fecha() == fecha:
                contador += 1
            elif isinstance(aux.getDato(), embalaje) and aux.getDato().get_fecha() == fecha:
                contador1 += 1
            aux = aux.getSiguiente()
        if contador > contador1:
            print("En esa fecha se hicieron mas servicios de transporte que de embalaje")
        elif contador1 > contador:
            print("En esa fecha se hicieron mas servicios de embalaje que de transporte")

    



