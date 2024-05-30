from claseservicio import servicio
class embalaje(servicio):
    __precio_unidad:float
    __peso_unidad:int
    __cantidad_unidades:int

    def __init__(self,nombre_servicio,nombre_contratante,direccion,fecha,comision,precio_unidad,peso_unidad,cantidad):
        super().__init__(nombre_servicio,nombre_contratante,direccion,fecha,comision)
        self.__precio_unidad=precio_unidad
        self.__peso_unidad=peso_unidad
        self.__cantidad_unidades=cantidad

    def get_precio_unidad(self):
        return self.__precio_unidad
    
    def get_peso(self):
        return self.__peso_unidad
    
    def get_cantidad_unidades(self):
        return self.__cantidad_unidades
    
    def __str__(self):
        return f"Nombre servicio: {self.get_nombre_servicio()}, Nombre del contratante{self.get_nombre_contratante()}, Direccion: {self.get_direccion()}, Fecha {self.get_fecha()}, Comision: {self.get_comision()}, Precio por unidad {self.__precio_unidad}, Peso unidad: {self.__peso_unidad}, Cantidad de unidades: {self.__cantidad_unidades}"
    
    def get_paquete_mayor_a_50(self):
        contador=0
        if self.__peso_unidad > 50:
            contador+=1
        return contador
    