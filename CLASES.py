class Personas:
    def __init__(self,crear,listar,eliminar,actualizar):
        self.personas = ["juan","jorge"]
        self.crear = crear
        self.listar = listar
        self.eliminar = eliminar
        self.actualizar = actualizar
        

    def crear_p(self):
        nombre = input("Ingrese el nombre de la persona: ")
        self.personas.append(nombre)
        print(f"Persona {nombre} creada exitosamente.")

    def listar_p(self):
        print("Lista de personas:")
        print(self.personas)
        
    def eliminar_p(self):
        nombre = input("Ingrese el nombre de la persona a eliminar: ")
       
        self.personas.remove(nombre)
        print(f"Persona {nombre} eliminada.")
        
    def ACTUALIZAR_p(self):
        
        actualizar = int(input("ingrese la posicion o coordenada del elemento que quiere cambiar "))
        nuevo = input("ingrese el nuevo nombre: ")
        self.personas[actualizar] = nuevo
        print(self.personas)
        
        
class UNIVERSIDADES:
    def __init__(self,crear,listar,eliminar,actualizar):
        self.universidades = ["tecnar","utb"]
        self.crear = crear
        self.listar = listar
        self.eliminar = eliminar
        self.actualizar = actualizar
        

    def crear_u(self):
        nombre = input("Ingrese el nombre de la universidad: ")
        self.universidades.append(nombre)
        print(f"universidad {nombre} creada exitosamente.")

    def listar_u(self):
        print("Lista de universidades:")
        print(self.universidades)
        
    def eliminar_u(self):
        nombre = input("Ingrese el nombre de la universidad a eliminar: ")
       
        self.universidades.remove(nombre)
        print(f"universidad {nombre} eliminada.")
        
    def ACTUALIZAR_u(self):
        
        actualizar = int(input("ingrese la posicion o coordenada del elemento que quiere cambiar "))
        nuevo = input("ingrese el nuevo nombre: ")
        self.universidades[actualizar] = nuevo
        print(self.universidades)
        
class NOTA:
    def __init__(self,crear,listar,eliminar,actualizar):
        self.notas = [1,2]
        self.crear = crear
        self.listar = listar
        self.eliminar = eliminar
        self.actualizar = actualizar
        

    def crear_n(self):
        nombre = int(input("Ingrese una nota: "))
        self.notas.append(nombre)
        print(f"nota {nombre} agregada exitosamente.")

    def listar_n(self):
        print("Lista de notas: ")
        print(self.notas)
        
    def eliminar_n(self):
        nombre = int(input("Ingrese la nota a eliminar: "))
       
        self.notas.remove(nombre)
        print(f"nota {nombre} eliminada.")
        
    def ACTUALIZAR_n(self):
        
        actualizar = int(input("ingrese la posicion o coordenada del elemento que quiere cambiar "))
        nuevo = input("ingrese la nueva nota: ")
        self.notas[actualizar] = nuevo
        print(self.notas)
        
class ASIGNATURAS:
    def __init__(self,crear,listar,eliminar,actualizar):
        self.asignatura= ["electronica","programacion"]
        self.crear = crear
        self.listar = listar
        self.eliminar = eliminar
        self.actualizar = actualizar
        

    def crear_a(self):
        nombre = input("Ingrese el nombre de la asignatura: ")
        self.asignatura.append(nombre)
        print(f"asignatura {nombre} creada exitosamente.")

    def listar_a(self):
        print("Lista de asignaturas:")
        print(self.asignatura)
        
    def eliminar_a(self):
        nombre = input("Ingrese el nombre de la asignatura a eliminar: ")
       
        self.asignatura.remove(nombre)
        print(f" asignatura {nombre} eliminada.")
        
    def ACTUALIZAR_a(self):
        
        actualizar = int(input("ingrese la posicion o coordenada del elemento que quiere cambiar "))
        nuevo = input("ingrese el nuevo nombre: ")
        self.asignatura[actualizar] = nuevo
        print(self.asignatura)
            

