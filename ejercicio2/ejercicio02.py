"Considere los objetos siguientes:"
"Animal"
"Mamífero"
"Ovíparo"
"Pollo"
"Gato"
"Ornitorrinco"
"Describa las relaciones entre los diferentes objetos. El diagrama asociado se llama diagrama de clases."
"Dar un ejemplo de descripción algorítmica de las clases asociadas (únicamente la declaración de clase XXX)."
"¿Es posible implementar estos objetos en Python?"

class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def get_nombre(self):
        return self.nombre
    def get_especie(self):
        return self.especie

nombre = input ("Introduzca el nombre del animal: ")
especie = input ("Introduzca la especie del animal: ")

print(Animal)

class Mamifero(Animal):
    def __init__(self, nombre, especie, pelaje):
        super().__init__(nombre, especie)
        self.pelaje = pelaje

    def get_pelaje(self):
        return self.pelaje

nombre = input ("Introduzca el nombre del mamifero: ")
especie = input ("Introduzca la especie del mamifero: ")
pelaje = input ("Introduzca el pelaje del mamifero: ")

print(Mamifero)

class Oviparo(Animal):
    def __init__(self, nombre, especie, huevos):
        super().__init__(nombre, especie)
        self.huevos = huevos

    def get_huevos(self):
        return self.huevos

nombre = input ("Introduzca el nombre del oviparo: ")
especie = input ("Introduzca la especie del oviparo:")
huevos = input ("Introduzca el numero de huevos del oviparo: ")

print(Oviparo)

class Pollo(Oviparo):
    def __init__(self, nombre, especie, huevos, plumas):
        super().__init__(nombre, especie, huevos)
        self.plumas = plumas

    def get_plumas(self):
        return self.plumas

nombre = input ("Introduzca el nombre del pollo: ")
especie = input ("Introduzca la especie del pollo: ")
huevos = input ("Introduzca el numero de huevos del pollo: ")
plumas = input ("Introduzca el numero de plumas del pollo: ")

print(Pollo)

def Gato(Mamifero):
    def __init__(self, nombre, especie, pelaje, orejas):
        super().__init__(nombre, especie, pelaje)
        self.orejas = orejas

    def get_orejas(self):
        return self.orejas

nombre = input ("Introduzca el nombre del gato: ")
especie = input ("Introduzca la especie del gato: ")
pelaje = input ("Introduzca el pelaje del gato: ")
orejas = input ("Introduzca el numero de orejas del gato: ")

print(Gato)

class Ornitorrinco(Mamifero):
    def __init__(self, nombre, especie, pelaje, pico):
        super().__init__(nombre, especie, pelaje)
        self.pico = pico

    def get_pico(self):
        return self.pico

nombre = input ("Introduzca el nombre del ornitorrinco: ")
especie = input ("Introduzca la especie del ornitorrinco: ")
pelaje = input ("Introduzca el pelaje del ornitorrinco: ")
pico = input ("Introduzca el pico del ornitorrinco: ")

print(Ornitorrinco)