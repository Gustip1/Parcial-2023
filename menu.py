from claselistaservicio import lista
class unmenu:
    def __init__(self):
        self.GL=lista()

    def run(self):
        while True:
            a = input("""MENU DE OPCIONES
                    1 para hacer carga:
                    2 para hacer el item a 
                    3 para hacer el item b
                    4 para hacer el item c
                    5 para salir
                        """)
            if a == '1':
                self.GL.carga()
                self.GL.mostar()
            elif a =='2':
                self.GL.mostar_servicio_transporte()
            elif a =='3':
                self.GL.paquetes_50_kilos()
            elif a == '4':
                fecha=input("ingrese una Fecha: ")
                self.GL.servicio_con_mas_contrataciones(fecha)
            elif a == '5':
                break
            