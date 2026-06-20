from metaclase import Metaclase

class Usuario(metaclass = Metaclase):
    def __init__(self, nombre, apellido, dni, correo_electronico):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.correo_electronico = correo_electronico
        self.activo = True
    def alta(self):
        self.activo = True
    def baja(self):
        self.activo = False

    def mostrar_datos(self):
        print(f'''
                Nombre: {self.nombre}
                Apellido: {self.apellido}
                DNI: {self.dni}
                Correo: {self.correo_electronico}
                Activo: {"Sí" if self.activo else "No"}
              ''')
        
class Lector(Usuario):
    def __init__(self, nombre, apellido, dni, correo_electronico, edad):
        super().__init__(nombre, apellido, dni, correo_electronico)
        self.edad = edad

    def mostrar_datos(self):
        print(f'''
                Nombre: {self.nombre}
                Apellido: {self.apellido}
                DNI: {self.dni}
                Correo: {self.correo_electronico}
                Edad: {self.edad}
                Activo: {"Sí" if self.activo else "No"}
              ''')    