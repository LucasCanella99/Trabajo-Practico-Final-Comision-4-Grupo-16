from metaclase import Metaclase
class Libro(metaclass = Metaclase):
    def __init__(self,titulo,autor,isbn,año_publicacion,cantidad_paginas,disponibilidad= True, activo= True): # Datos minimos(atributos), disponibilidad es si esta para prestar disponible para prestarlo. Activo es si esta disponible fisicamente(caso de romperse etc etc)
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.año_publicacion = año_publicacion
        self.cantidad_paginas = cantidad_paginas
        self.disponibilidad = disponibilidad
        self.activo = activo

    #Operaciones(métodos)

    def alta(self): # Esta disponible fisicamente
        self.activo = True
    
    def baja(self): # Se rompio, ser perdio, etc, en cualquier caso que no este disponible fisicamente
        self.activo = False

    def prestar(self): # Se prestó
        self.disponibilidad = False
    
    def devolucion(self): # Fue devuelto
        self.disponibilidad = True

    def modificacion(self,titulo,autor,isbn,año_publicacion,cantidad_paginas): # Lo interpretamos como modificar datos del libro
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.año_publicacion = año_publicacion
        self.cantidad_paginas = cantidad_paginas

    def mostrar_datos(self): # Es la operacion requerida listado, lo interpretamos como mostrar datos. El listado "real" de mostrar la cant de libros va a estar en la clase biblioteca, que es la contenedora de listas de objetos. 
        print(f'''
                Título: {self.titulo}
                Autor: {self.autor}
                ISBN: {self.isbn}
                Año de publicación: {self.año_publicacion}
                Cantidad de páginas: {self.cantidad_paginas}
                Disponible: {'Sí' if self.disponibilidad else 'No'}
              ''')
    
