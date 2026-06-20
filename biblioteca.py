from libro import Libro
#from usuario import Lector
#from prestamo import Prestamo



class Biblioteca: #Clase gestora/contenedora de listas, libros, usuarios, prestamos, etc etc
    def init(self):
        self.libros = []
        self.lectores = []
        self.prestamos = []
    #--------------------Libros--------------------------
    def agregar_libro(self,titulo,autor,isbn,año_publicacion,cantidad_paginas): # Por defecto disponibilidad y activo estan en True, se supone que si se agrega un libro nuevo es porque esta disponible.
        libro_nuevo = Libro(titulo,autor,isbn,año_publicacion,cantidad_paginas)
        self.libros.append(libro_nuevo)
        print("Nuevo libro agregado a la biblioteca!")

    def listar_libros(self): #Operacion listado requerida(Solo se muestran los disponibles)
        for libro in self.libros:
            if libro.disponibilidad == True:
                libro.mostrar_datos()
    
    def dar_baja_libro(self, isbn): #Se da de baja el libro por su isbn
        for libro in self.libros:
            if isbn == libro.isbn:
                libro.baja()
                print("Libro encontrado y dado de baja!")
                return
        print("Libro no encontrado, revise ISBN e intenta nuevamente.")

    def dar_alta_libro(self,isbn): #Se "vuelve" a dar de alta un libro.
        for libro in self.libros:
            if isbn == libro.isbn:
                libro.alta()
                print("Libro encontrado y dado de alta!")
                return
        print("Libro no encontrado, revise ISBN e intenta nuevamente.")
    #-------------------Gestión de prestamos---------------------
    def prestar_libro(self,isbn,dni):
        libro_buscado = None
        lector_buscado= None

        for libro in self.libros: #Se busca al libro y que este disponible
            if libro.isbn == isbn and libro.activo== True and libro.disponibilidad == True:
                libro_buscado = libro
                break
        else:
            print("Libro no disponible.")
            return

        for lector in self.lectores: #Se busca al lector(usuario)
            if lector.dni == dni:
                lector_buscado = lector
                break
        else: 
            print("Usuario no encontrado.")
            return
        #Si se encontró el libro y el usuario
        libro_buscado.prestar()
        #nuevo_prestamo = Prestamo(libro_buscado,lector_buscado) #Registramos el prestamo
        #self.prestamos.append(nuevo_prestamo) #Se agrega a la lista de prestamos
        print("Prestamo registrado!")

    def devolver_libro(self,isbn):
        for prestamo in self.prestamos:
            if prestamo.libro.isbn == isbn and prestamo.activo == True: #Recorremos la lista de prestamos y buscamos uno que coincida 
                prestamo.devolver()
                prestamo.libro.devolucion()
                print("Devolución del préstamo registrada!")
                return
        print("No se encontro un prestamo de ese libro!")
        
    def listar_prestamos(self): #Operacion listado de prestamos
        for prestamo in self.prestamos:
            if prestamo.activo == True:
                prestamo.mostrar_datos()

    #-----------Usuarios-------------
    def listar_usarios(self): #Operacion listado de usaurio (REQUERIDA)
        for lector in self.lectores:
                lector.mostrar_datos()

    def agregar_usuario(self):
        #nuevo_lector = Lector(nombre,apellido,dni,corre_electronico)
        #self.lectores.append(nuevo_lector)
        #print("Usuario registrado!")   
        pass

    def dar_baja_usuario(self,dni):
        for lector in self.lectores:
            if lector.dni == dni and lector.activo == True:
                lector.baja()
                print("Usuario dado de baja!")
                return
        print("Usuario no encontrado!")

    def dar_alta_usuario(self,dni):
        for lector in self.lectores:
            if lector.dni == dni and lector.activo == False:
                lector.alta()
                print("Usuario dado de alta!")
                return
        print("Usuario no encontrado!")
    
    #Decorador de recordatorio de prestamos. Es un decorador que cumple el PATRON DE DISEÑO OBSERVER que es cuando el bibliotecario quiere enviar un recordatorio a todos los usuarios del prestamo activo ejecuta la opcion de notificar a los "deudores" de prestamos activos de libros con la funcion enviar_recordatorios. Es una simulacion obviamente. Se utiliza en el menu de interfaz interactivo por consola. Cumple el patron de diseño porque busca a cada usuario del sistema los lectores con prestamos activos y los "notifica(sin olvidar que es una simulacion)" uno por uno por mail. 

    
    def notificar_prestamos_activos(func):
        def wrapper(self, *args, **kwargs):
            for prestamo in self.prestamos:
                if prestamo.activo:
                    print(f"Email enviado a {prestamo.lector.correo_electronico} - Recordatorio: tenes un préstamo activo del libro '{prestamo.libro.titulo}', si ya terminaste de leerlo recordá devolverlo.")
            return func(self, *args, **kwargs)
        return wrapper

    @notificar_prestamos_activos
    def enviar_recordatorios(self):
        pass
    

            
        

    