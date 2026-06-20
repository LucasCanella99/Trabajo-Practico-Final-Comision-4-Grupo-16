from metaclase import Metaclase
from datetime import date
 
class Prestamo(metaclass = Metaclase):
    def __init__(self, libro, lector):
        self.libro = libro
        self.lector = lector
        self.fecha_prestamo = date.today()
        self.fecha_devolucion = None
        self.activo = True
 
    def devolver(self):
        self.fecha_devolucion = date.today()
        self.activo = False
 
    def mostrar_datos(self):
        print(f'''
                Libro: {self.libro.titulo}
                Lector: {self.lector.nombre} {self.lector.apellido}
                Fecha de préstamo: {self.fecha_prestamo}
                Fecha de devolución: {self.fecha_devolucion if self.fecha_devolucion else "No devuelto aún"}
                Estado: {"Activo" if self.activo else "Devuelto"}
              ''')
 