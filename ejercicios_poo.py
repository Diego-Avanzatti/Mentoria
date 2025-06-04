class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años")
    
# persona_1 = Persona("diego",33)
# print(f"Mi nombre es {persona_1.nombre} y tengo {persona_1.edad}")
# persona_1.presentarse()


class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        print(f"{self.nombre}: ${self.precio}. Stock: {self.stock}")

    def vender(self):
        if self.stock > 0:
            self.stock -= 1
            print(f"Producto vendido. Quedan {self.stock} unidades.")
        else:
            print("No hay más stock disponible.")

# producto_1 = Producto("harina", 1200, 10)
# producto_2 = Producto("pan", 1000, 12)
# producto_3 = Producto("azucar", 1500, 10)
# producto_4 = Producto("vino", 3200, 5)


class Inventario:
    def __init__(self):
        self.lista_productos = []
    
    def agregar_producto(self, producto):
        self.lista_productos.append(producto)
        print("Producto agregado...")

    def mostrar_productos(self):
        for producto in self.lista_productos:
            producto.mostrar_info()

    def buscar_producto(self, nombre):
        encontrado = False
        for producto in self.lista_productos:
            if nombre.lower().strip() == producto.nombre.lower().strip():
                producto.mostrar_info()
                encontrado = True
                break
        if not encontrado:
            print("Producto no encontrado")

# inventario1 = Inventario()
# inventario1.agregar_producto(producto_1)
# inventario1.agregar_producto(producto_2)
# inventario1.agregar_producto(producto_3)
# inventario1.agregar_producto(producto_4)
# inventario1.mostrar_productos()
# inventario1.buscar_producto("carbon")



            

class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera
    
    def datos_estudiante(self):
        print(f"Soy {self.nombre}, tengo {self.edad} años y estudio {self.carrera}.")

# estudiante_1 = Estudiante("juan", 35, "programacion")
# estudiante_1.datos_estudiante()

class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca 
        self.modelo = modelo

    def arrancar(self):
        print("El vehículo está en marcha.")

class Moto(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    
    def hacer_wheelie(self):
        print("Haciendo wheelie!!!")

    def tipo_vehiculo(self):
        print("soy una moto")

class Auto(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
    
    def tocar_vocina(self):
        print("beet beeeet!!!!")

    def tipo_vehiculo(self):
        print("soy un auto")

# auto1 = Auto("toyota","corolla")
# auto1.arrancar()
# auto1.tocar_vocina()

# moto1 = Moto("honda", "wave")
# moto1.arrancar()
# moto1.hacer_wheelie()

# lista_vehiculo = [
#     Auto("toyota", "corolla"),
#     Moto("honda", "wave"),
#     Auto("toyota", "hillux"),
#     Moto("honda", "tornada"),
#     Auto("toyota", "yaris"),
#     Moto("honda", "XR"),
#     Auto("renault", "clio"),
#     Moto("Zanella", "150")
# ]


# for i in lista_vehiculo:
#     i.tipo_vehiculo()

