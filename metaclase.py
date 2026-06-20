class Metaclase(type): #Usamos de type la creacion de clase y ahora es una metaclase "nueva"
    def __new__(cls, nombre, bases, dict): #__new__ crea el objeto y si mostrar_datos no esta implementado levanta un typeError.
        if 'mostrar_datos' not in dict:
            raise TypeError(f"La clase {nombre} debe implementar mostrar_datos()")
        return type(nombre, bases, dict)
    

    #cls es como self, toma el objeto como si fuera una instancia de la metaclase. Y dict es su "lista o dict" de metodos implementados si no encuentra el mostrar datos levanta el error, esto cumple el requerimiento de metaclase porque se modifica la metaclase "type" y se crea una nueva metaclase obligando a implentar a mostrar_datos a todas las clases que usen esta metaclase en vez de type como lo harian por defecto para crear la clase normalmente.
    # Por eso al crear la clase se le pasa como parametro de metaclass esta Metaclase y no por defecto solo type. Es como type pero modificada para este contexto