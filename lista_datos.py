# Crear una lista llamada Datos_personales
Datos_personales = []

# Agregar datos a la lista utilizando append()
nombre = input("Ingrese el nombre: ")
edad = int(input("Ingrese la edad: "))
altura = float(input("Ingrese la altura (en metros): "))
estado_civil = input("Ingrese el estado civil: ")
direccion = input("Ingrese la dirección: ")

# Agregar los datos a la lista
Datos_personales.append(nombre)
Datos_personales.append(edad)
Datos_personales.append(altura)
Datos_personales.append(estado_civil)
Datos_personales.append(direccion)

# Mostrar el contenido de la lista
print("Datos personales:")
print("Nombre:", Datos_personales[0])
print("Edad:", Datos_personales[1])
print("Altura:", Datos_personales[2])
print("Estado civil:", Datos_personales[3])
print("Dirección:", Datos_personales[4])
