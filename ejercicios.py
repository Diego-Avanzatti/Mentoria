# 1- Crea una lista con los números del 1 al 5. Muestra el contenido de la lista por pantalla.
# 2- Crea una lista vacía. Agrega los nombres "Ana", "Luis" y "Carlos" usando el método append() y luego imprime la lista.
# 3- Dada la lista frutas = ["manzana", "banana", "naranja"], cambia el segundo elemento por "pera" y muestra la lista modificada.
# 4- Crea una tupla con tres colores: "rojo", "verde", "azul". Muestra el segundo color.
# 5- Dada la tupla datos = (10, 20, 30), conviértela en una lista, agrega el número 40, y vuelve a convertirla en tupla.
# 6- Dada la tupla numeros = (1, 2, 2, 3, 4, 2), cuenta cuántas veces aparece el número 2.
# 7- Crea un conjunto a partir de la lista nombres = ["Ana", "Luis", "Ana", "Carlos"] y muestra el resultado.
# 8- Crea un conjunto con los números del 1 al 5. Pregunta si el número 3 está en el conjunto.
# 9- Dado A = {1, 2, 3} y B = {3, 4, 5}, muestra la intersección de ambos conjuntos.
# 10- Crea un diccionario con claves "nombre", "edad" y "ciudad", con tus propios datos. Muestra el valor de "ciudad".
# 11- Dado el diccionario alumno = {"nombre": "Lucía", "nota": 7}, cambia la nota a 9 y agrega la clave "aprobado" con el valor True.
# 12- Dado el diccionario colores = {"rojo": "red", "azul": "blue", "verde": "green"}, muestra todas las claves y valores uno por uno.

#1-
print("\n1_\n")
numeros = [1,2,3,4,5]
#Muestra lista de numeros
print(numeros)

# Muestra los numeros de la lista
for i in numeros:
    print(i)

#2-
print("\n2_\n")
nombres = []

nombres.append("Ana")
nombres.append("Luis")
nombres.append("Carlos")

print(nombres)

#3-
print("\n3_\n")
frutas = ["manzana", "banana", "naranja"]

frutas[1] = "pera"

print(frutas)

#4-
print("\n4_\n")
colores = ("rojo", "verde", "azul")

print(colores[1])

#5-
print("\n5_\n")
datos = (10, 20, 30)

datos_lista = list(datos)
datos_lista.append(40)

datos = tuple(datos_lista)

print(datos)

#6-
print("\n6_\n")
numeros = (1, 2, 2, 3, 4, 2)

contador = 0

for i in numeros:
    if i == 2:
        contador += 1

print(f"el numero 2 aparece {contador} veces.")

#7-
print("\n7_\n")
nombres = ["Ana", "Luis", "Ana", "Carlos"]

nombres_conjunto = set(nombres)
print(nombres_conjunto)

#8-
print("\n8_\n")
numeros = {1,2,3,4,5}

if 3 in numeros:
    print("El numero 3 esta en el conjunto.")
else:
    print("el numero 3 no se encuentra en el conjunto.")


#9-
print("\n9_\n")
A = {1, 2, 3}
B = {3, 4, 5}

interseccion = A & B

print(f"la interseccion entre A y B es:  {interseccion}")


#10-
print("\n10_\n")
persona = {
    "nombre": "Diego",
    "edad": 33,
    "ciudad": "Villa Angela"
    }

print(f" Mi ciudad es {persona['ciudad']}")


#11-
print("\n11_\n")
alumno = {"nombre": "Lucía", "nota": 7}

alumno["nota"] = 9
alumno["aprobado"] = True

print(alumno)


#12-
print("\n12_\n")
colores = {"rojo": "red", "azul": "blue", "verde": "green"}

for clave, valor in colores.items():
    print(f"{clave}: {valor}")

print("\n")