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
#crear lista vacia
mi_lista = []

#longitud de la lista
lst = [1, 2, 3, 4, 5]
longitud_mi_lista = len(lst)

lst = list(range(1, 11))
longitud_otra_lista = len(lst)
#crear empresas Ejer 6
lst = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# craear una lista con 5 elementos ejer 2
lst = ['amarillo', 'azul', 'rojo', 'vinotinto', 'verde']
lst = list(range(1, 11))
# añadir una empresa it, ejer 7
# Lista original
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Agregar una nueva empresa (por ejemplo, "Intel") en la posición deseada (índice 2)
it_companies.insert(2, "AMD")

# La lista actualizada
print(it_companies)

#comprobar si una empresa existe ejer 8
# Lista original
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Empresa a verificar (por ejemplo, "Google")
empresa_a_verificar = "Google"

# Comprobar si la empresa está en la lista
if empresa_a_verificar in it_companies:
    print(f"{empresa_a_verificar} está en la lista.")
else:
    print(f"{empresa_a_verificar} no está en la lista.")

# ordenar la lista con sort ejer 9
    # Lista original
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Ordenar la lista en orden alfabético
it_companies.sort()

# La lista ordenada
print(it_companies)

# invertir lista ejer 10
# Lista original
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Invertir la lista en orden descendente
it_companies.reverse()

# La lista invertida
print(it_companies)

# Eliminar primera empresa usando pop y delete
# Lista original (restaurada para este ejemplo)
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Eliminar la primera empresa (Facebook) utilizando del
del it_companies[0]

# La lista actualizada sin la primera empresa
print("Lista actualizada:", it_companies)

# ejer 12
# Lista original
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# Vaciar la lista (eliminar todas las empresas)
it_companies.clear()

# Verificar que la lista está vacía
print("Lista de empresas después de eliminar todas:", it_companies)
