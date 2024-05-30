from claseservicio import servicio
class transporte(servicio):
    __precio_por_hora:float
    __peso_carga:int
    __direcion_de_destino:str

    def __init__(self,nombre_servicio,nombre_contratante,direccion,fecha,comision,precio_hora,peso,direccion_destino):
        super().__init__(nombre_servicio,nombre_contratante,direccion,fecha,comision)
        self.__precio_por_hora=precio_hora
        self.__peso_carga=peso
        self.__direcion_de_destino=direccion_destino

    def get_precio_hora(self):
        return self.__precio_por_hora
    def get_peso_carga(self):
        return self.__peso_carga
    def get_direccion_destino(self):
        return self.__direcion_de_destino
    
    def __str__(self):
        return f"Nombre servicio: {self.get_nombre_servicio()}, Nombre del contratante{self.get_nombre_contratante()}, Direccion: {self.get_direccion()}, Fecha {self.get_fecha()}, Comision: {self.get_comision()}, Precio por hora: {self.__precio_por_hora}, Peso carga: {self.__peso_carga}, Direccion de destino: {self.__direcion_de_destino}"
    
    def get_coste_total(self):
        coste_total= (self.__precio_por_hora + self.get_comision())
        return coste_total
    