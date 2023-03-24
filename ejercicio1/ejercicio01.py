"Escriba una clase que permita describir un libro y situar los valores asociados. Dar un ejemplo de uso en Python"

class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.genero = genero
        self.año_publicacion = año_publicacion

    def get_titulo(self):
        return self.titulo
    def get_autor(self):
        return self.autor
    def get_paginas(self):
        return self.paginas
    def get_genero(self):
        return self.genero
    def get_año_publicacion(self):
        return self.año_publicacion

titulo = input ("Introduzca el titulo del libro: ")
autor = input ("Introduzca el autor del libro: ")
paginas = int(input ("Introduzca el numero de paginas del libro: "))
genero = input ("Introduzca el genero del libro: ")
año_publicacion = input ("Introduzca el año de publicacion del libro: ")

print(Libro)