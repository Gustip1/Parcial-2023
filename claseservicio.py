class servicio:
    __nombre_servicio:str
    __nombre_del_contratante:str
    __direccion_del_contratante:str
    __fecha:str
    __comision: int

    def __init__(self,nombre_servicio,nombre_contratante,direccion,fecha,comision):
        self.__nombre_servicio=nombre_servicio
        self.__nombre_del_contratante=nombre_contratante
        self.__direccion_del_contratante=direccion
        self.__fecha=fecha
        self.__comision=comision
    
    def get_nombre_servicio(self):
        return self.__nombre_servicio
    def get_nombre_contratante(self):
        return self.__nombre_del_contratante
    def get_direccion(self):
        return self.__direccion_del_contratante
    def get_fecha(self):
        return self.__fecha
    def get_comision(self):
        return self.__comision
    
    def __str__(self):
        return f"Nombre servicio: {self.__nombre_servicio}, Nombre del contratante{self.__nombre_del_contratante}, Direccion: {self.__direccion_del_contratante}, Fecha: {self.__fecha}, Comision: {self.__comision}"
    