# # frutas = {
# #     "manzana": 124.50,
# #     "pera": 12.5,
# #     "uva": 23.4
# #     }

# # # print(frutas)

# # # for clave, valor in frutas.items():
# # #     print(f"{clave}: ${valor}")

# # for indice,fruta in enumerate(frutas.items(),1):
# #     print(f"{indice}_{fruta[0]}: $ {fruta[1]}")

# #----------------------------------------------------------------


# # ciudades = ["resistencia","villa angela","santa sylvina"]

# # mas_ciudades = ciudades.copy()
# # mas_ciudades.append("barranqueras")

# # for i in  ciudades:
# #     print(i)
# # print("\n")

# # for i in  mas_ciudades:
# #     print(i)


# #------------------------------------------------
# # paises = ["argentina", "francia", "brasil"]
# # print(paises[1])

# #----------------------------------------------

# # personas = {
# #     "Juan": 18,
# #     "Pedro": 23,
# #     "Luis": 30
# #     }


# # print(f"La edad de Luis es: {personas["Luis"]}")


# #------------------------------------------------------
# # numeros = {1,2,3,4,5,6}

# # lista_numeros = list(numeros)
# # ultimo = lista_numeros[-1]
# # print(f"El ultimo numero del set es: {ultimo}")

# #--------------------------------------------------------

# # lista = []

# # for i in range(1,11):
# #     if i %2 == 1:
# #        lista.append(i)

# # set = set(lista)

# # print(set)
# # print(f"el numero de elementos en el set es de {len(set)}")

# # mi_set = set()

# # for i in range(1,11):
# #     if i%2 == 1:
# #         mi_set.add(i)

# # print(mi_set)
# # print(len(mi_set))


# #-------------------------------------------------
# # ciudades = {
# #     "resistencia": 900000,
# #     "villa angela": 100000,
# #     "santa sylvina": 90000
# # }


# # ciudades["plaza"] = 30000

# # for i, ciudad in enumerate(ciudades.items(),1):
# #     print(f"{i}_ {ciudad[0]}: {ciudad[1]}")

# #------------------------------------------------------

# # numeros = []

# # for i in range(1,11):
# #     numeros.append(i)


# # # print(numeros[::-1])

# # numeros.reverse()

# # print(numeros)

# #--------------------------------------------------------

# # paises = ["argentina", "francia", "Brasil"]

# # paises_ordenados = []

# # for i in paises:
# #     paises_ordenados.append(i.capitalize())

# # paises_ordenados.sort()
# # paises.sort()
# # print(paises_ordenados)
# # print(paises)

# #---------------------------------------------------------
# # frutas = ["manzana","pera","uva"]

# # frutas.pop(1)

# # print(frutas)

# #---------------------------------------------------------

# # animales = ["perro", "gato", "vaca"]

# # animales.insert(0,"caballo")

# # print(animales)


# #-------------------------------------------------------

# # paises = ["argentina", "francia", "Brasil"]

# # paises[1] = "peru"
# # print(paises)

# # colores = ["rojo","azul","verde"]

# # #colores[3:] = ("amarillo", "naranja")

# # colores.extend(["naranja","negro"])

# # print(colores)

# #-------------------------------------------------------

# # tupla = (1,2,3,4,5)

# # # suma = 0
# # # for i in tupla:
# # #     suma += i

# # # print(suma)

# # suma = sum(tupla)
# # print(suma)


# Ejercicios nuevos:

# Crear una lista con los nombres de tres libros y agregar un cuarto libro al final.

# libros = ["libro_1", "libro_2", "libro_3"]

# libros1 = libros.copy()
# libros1.append("libro")
# print(libros1)


# Crear un diccionario con tres marcas de autos y su país de origen. Mostrar el país de origen de una marca específica.

# autos = {
#     "BMW": "Alemania",
#     "toyota": "Japon",
#     "ferrari": "Italia"
# }

# marca = autos["ferrari"]
# print(f"La ciudad de la marca es {marca}")

# Crear una tupla con cinco números y mostrar el menor valor.

# numeros = (2,3,4,5)
# menor = min(numeros)
# print(f"El menor de la tupla es {menor}")

# Crear un set con los días de la semana y eliminar un día. Mostrar el set resultante.

# semana = ("lunes", "martes", "miercoles", "jueves", "viernes", "s", "d")
# lista_semana = list(semana)
# lista_semana.pop(2)
# lista_semana.remove("lunes")
# semana_nueva = tuple(lista_semana)
# print(semana_nueva)

# Crear una lista con tres nombres y verificar si un nombre específico está en la lista.

# nombres = ["diego", "matias", "mauro"]
# print("diego" in nombres)


# Crear un diccionario con tres animales y su tipo (mamífero, ave, etc.). Agregar un cuarto animal.

# animales = {
#     "perro": "mamifero",
#     "loro": "ave",
#     "gato": "felino"
# }

# animales["vaca"] = "mamifero"

# for clave, valor in animales.items():
#     print(f"{clave}: {valor}.")

# Crear una lista con cinco números y calcular el promedio.

# lista = [1,2,3,4,5]
# promedio = sum(lista) /len(lista)

# print(f"El promedio de la lista es {promedio}")


# Crear un set con letras de una palabra y mostrar cuántas letras diferentes tiene.

# texto = "Hola como estamos"
# palabra = texto.replace(" ","")
# letras = set(palabra)
# print(f" hay {len(letras)} letras diferentes")


# Crear una lista con los números del 1 al 5 y duplicar cada número. Mostrar la nueva lista.

# lista = [1,2,3,4,5]
# nueva_lista = []

# for i in lista:
#     duplicado = i * 2
#     nueva_lista.append(duplicado)

# print(nueva_lista)
# print(lista)

# Crear un diccionario con los nombres de tres materias y sus respectivas notas. Calcular el promedio de las notas.

# notas = {
#     "fsica": 7,
#     "matematicas": 5,
#     "quimica": 8
# }

# promedio = sum(notas.values())/len(notas)
# print(f"El promedio de las notas es de {promedio:.2f}")

# # Crear una tupla con tres colores y mostrar el segundo color.

# colores = ("azul", "rojo", "verde")

# print(colores[1])

# Crear una lista vacía y agregarle tres elementos uno por uno.
# lista = []

# lista.append("hola")
# lista.append("hola")
# lista.append("hola")
# print(lista)

# Crear un set con los números del 1 al 5 y agregar el número 6. Mostrar el set resultante.

# set = {1,2,3,4,5}

# set.add(6)
# print(set)

# Crear un diccionario con tres países y sus capitales. Reemplazar la capital de uno de los países.

# paises = {
#     "Argentina": "buenos aires",
#     "paraguay": "asuncion",
#     "bolivia": "la paz"
# }

# paises["Argentina"] = "Chaco"

# print(paises)

