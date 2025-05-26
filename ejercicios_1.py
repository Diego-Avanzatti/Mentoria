# frutas = {
#     "manzana": 124.50,
#     "pera": 12.5,
#     "uva": 23.4
#     }

# # print(frutas)

# # for clave, valor in frutas.items():
# #     print(f"{clave}: ${valor}")

# for indice,fruta in enumerate(frutas.items(),1):
#     print(f"{indice}_{fruta[0]}: $ {fruta[1]}")

#----------------------------------------------------------------


# ciudades = ["resistencia","villa angela","santa sylvina"]

# mas_ciudades = ciudades.copy()
# mas_ciudades.append("barranqueras")

# for i in  ciudades:
#     print(i)
# print("\n")

# for i in  mas_ciudades:
#     print(i)


#------------------------------------------------
# paises = ["argentina", "francia", "brasil"]
# print(paises[1])

#----------------------------------------------

# personas = {
#     "Juan": 18,
#     "Pedro": 23,
#     "Luis": 30
#     }


# print(f"La edad de Luis es: {personas["Luis"]}")


#------------------------------------------------------
# numeros = {1,2,3,4,5,6}

# lista_numeros = list(numeros)
# ultimo = lista_numeros[-1]
# print(f"El ultimo numero del set es: {ultimo}")

#--------------------------------------------------------

# lista = []

# for i in range(1,11):
#     if i %2 == 1:
#        lista.append(i)

# set = set(lista)

# print(set)
# print(f"el numero de elementos en el set es de {len(set)}")

# mi_set = set()

# for i in range(1,11):
#     if i%2 == 1:
#         mi_set.add(i)

# print(mi_set)
# print(len(mi_set))


#-------------------------------------------------
# ciudades = {
#     "resistencia": 900000,
#     "villa angela": 100000, 
#     "santa sylvina": 90000
# }


# ciudades["plaza"] = 30000

# for i, ciudad in enumerate(ciudades.items(),1):
#     print(f"{i}_ {ciudad[0]}: {ciudad[1]}")

#------------------------------------------------------

# numeros = []

# for i in range(1,11):
#     numeros.append(i)


# # print(numeros[::-1])

# numeros.reverse()

# print(numeros)

#--------------------------------------------------------

# paises = ["argentina", "francia", "Brasil"]

# paises_ordenados = []

# for i in paises:
#     paises_ordenados.append(i.capitalize())

# paises_ordenados.sort()
# paises.sort()
# print(paises_ordenados)
# print(paises)

#---------------------------------------------------------
# frutas = ["manzana","pera","uva"]

# frutas.pop(1)

# print(frutas)

#---------------------------------------------------------

# animales = ["perro", "gato", "vaca"]

# animales.insert(0,"caballo")

# print(animales)


#-------------------------------------------------------

# paises = ["argentina", "francia", "Brasil"]

# paises[1] = "peru"
# print(paises)

# colores = ["rojo","azul","verde"]

# #colores[3:] = ("amarillo", "naranja")

# colores.extend(["naranja","negro"])

# print(colores)

#-------------------------------------------------------

# tupla = (1,2,3,4,5)

# # suma = 0
# # for i in tupla:
# #     suma += i

# # print(suma)

# suma = sum(tupla)
# print(suma)