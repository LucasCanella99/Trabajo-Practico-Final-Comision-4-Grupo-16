# Trabajo-Practico-Final-Comision-4-Grupo-16
# Sistema de Gestión de Biblioteca Digital

## Descripción
Sistema de gestión de biblioteca digital desarrollado en Python utilizando Programación Orientada a Objetos. Permite administrar libros, usuarios y préstamos a través de una interfaz interactiva por consola. Al iniciar el programa se simula que lo utiliza el bibliotecario, que puede realizar todas las operaciones del sistema.

## Integrantes
- Blanco, Pablo
- Canella, Lucas
- Soruco, Walter Ricardo

## Instrucciones para ejecutar
1. Clonar el repositorio
2. Acceder a la carpeta del proyecto
3. Ejecutar el programa con Python 3 por consola (comando: python3 menu.py)


## Estructura del sistema
- libro.py: Clase Libro con sus atributos y operaciones
- usuario.py: Clases Usuario y Lector
- prestamo.py: Clase Prestamo
- biblioteca.py: Clase Biblioteca, gestora central del sistema
- metaclase.py: Metaclase
- menu.py: Interfaz interactiva por consola

## Requerimientos técnicos

### Herencia
La clase "Lector" hereda de "Usuario", reutilizando sus atributos base (nombre, apellido, DNI, correo electrónico) y agregando el atributo "edad" de la clase lector.

### Polimorfismo
Las clases "Libro", "Usuario" y "Lector" implementan el método "mostrar_datos()" cada una con su propio comportamiento, mostrando los atributos correspondientes a cada clase.

### Agregación
"Prestamo" referencia objetos "Libro" y "Lector" que existen de manera independiente. Si un préstamo es eliminado, el libro y el lector siguen existiendo en el sistema.

### Composición
"Biblioteca" contiene las listas de libros, lectores y préstamos. Estas listas son partes del sistema, si la instancia de Biblioteca desaparece, las listas también.

### Metaclase
Se implementó una metaclase "Metaclase" derivada de "type", obligando a todas las clases que la utilicen a implementar el método "mostrar_datos()". Si una clase no lo implementa, el programa lanza un "TypeError" al iniciarse.

### Patrón de diseño Observer
Se implementó mediante un decorador "notificar_prestamos_activos" que envuelve el método "enviar_recordatorios()". Al ejecutarse, recorre todos los préstamos activos y simula el envío de un mail de recordatorio a cada uno de los lectores, notificándole que tiene un préstamo pendiente de devolución. Es una correcta implementacion del patrón de diseño observer, ya que cumple con la condicion de que si ocurre una accion se "notifica" ó "avisa" a cada uno de los usuarios. Salvando las distancias que es una simulación obviamente y no se puede implementar totalmente funcional.

### Patrón de diseño Repository
La clase "Biblioteca" centraliza el acceso y gestión de todas las listas de objetos del sistema. Ningún módulo externo accede directamente a las listas de libros, usuarios o préstamos, toda operación se realiza a través de los métodos de "Biblioteca". Es una correcta implementacion del patrón de diseño Repository ya que cumple con aislar de la logica del acceso a los datos(aunque en este caso no sea una base de datos y sea la RAM) y tambien cumple con centralizar las operaciones CRUD(Crear, Leer, Actualizar, Eliminar) en una unica interfaz coherente que es menu.py que importa e interactua directamente con Biblioteca.