from biblioteca import Biblioteca
#Es un menu principal que se ejecuta en un bucle while,si se selecciona una opcion abre un submenu con otro bucle while. Es como dos bucles whiles anidados y si se rompe al volver del submenu se vuelve al original y si se rompe ese tambien se sale del programa. Es mejor esto que ejecutar constantmente el menu principal para volver porque se satura el sistema de ejecutar funciones constantemente sino. 
def menu():
    sistema = Biblioteca()
    
    while True:
        print("\n--- Sistema de Gestión de Biblioteca Digital ---")
        print("1. Gestión de libros")
        print("2. Gestión de usuarios")
        print("3. Gestión de préstamos")
        print("0. Salir")
        
        opcion = input("Elegí una opción: ")
        
        if opcion == "1":
            submenu_libros(sistema)
        elif opcion == "2":
            submenu_usuarios(sistema)
        elif opcion == "3":
            submenu_prestamos(sistema)
        elif opcion == "0":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida.")


def submenu_libros(sistema):
    while True:
        print("\n--- LIBROS ---")
        print("1. Agregar libro")
        print("2. Listar libros")
        print("3. Dar de baja")
        print("4. Dar de alta")
        print("0. Volver")
        
        opcion = input("Elegí una opción: ")
        
        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            anio = input("Año de publicación: ")
            paginas = input("Cantidad de páginas: ")
            sistema.agregar_libro(titulo, autor, isbn, anio, paginas)
        
        elif opcion == "2":
            sistema.listar_libros()
        
        elif opcion == "3":
            isbn = input("ISBN del libro a dar de baja: ")
            sistema.dar_baja_libro(isbn)
        
        elif opcion == "4":
            isbn = input("ISBN del libro a dar de alta: ")
            sistema.dar_alta_libro(isbn)
        
        elif opcion == "0":
            break
        
        else:
            print("Opción inválida.")

def submenu_usuarios(sistema):
    while True:
        print("\n--- Usuarios ---")
        print("1. Agregar usuario")
        print("2. Listar usuarios")
        print("3. Dar de baja")
        print("4. Dar de alta")
        print("0. Volver")
        
        opcion = input("Elegí una opción: ")
        
        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            dni = input("DNI: ")
            correo_electronico = input("Correo electrónico: ")
            sistema.agregar_usuario(nombre, apellido, dni, correo_electronico)
        
        elif opcion == "2":
            sistema.listar_usuarios()
        
        elif opcion == "3":
            dni = input("DNI del usuario a dar de baja: ")
            sistema.dar_baja_usuario(dni)
        
        elif opcion == "4":
            dni = input("DNI del usuario a dar de alta: ")
            sistema.dar_alta_usuario(dni)
        
        elif opcion == "0":
            break
        
        else:
            print("Opción inválida.")

def submenu_prestamos(sistema):
    while True:
        print("\n--- Préstamos ---")
        print("1. Registrar préstamo")
        print("2. Registrar devolución")
        print("3. Listar préstamos activos")
        print("4. Enviar recordatorios")
        print("0. Volver")
        
        opcion = input("Elegí una opción: ")
        
        if opcion == "1":
            isbn = input("ISBN del libro: ")
            dni = input("DNI del lector: ")
            sistema.prestar_libro(isbn, dni)
        
        elif opcion == "2":
            isbn = input("ISBN del libro a devolver: ")
            sistema.devolver_libro(isbn)
        
        elif opcion == "3":
            sistema.listar_prestamos()
        
        elif opcion == "4":
            sistema.enviar_recordatorios()
        
        elif opcion == "0":
            break
        
        else:
            print("Opción inválida.")

menu()