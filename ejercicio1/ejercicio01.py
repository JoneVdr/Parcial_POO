#Escriba una clase que permita describir un libro y situar los valores asociados. Dar un ejemplo de uso en Python

class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.genero = genero

    def libro1(self):
        titulo = input ("Introduzca el titulo del libro: ")
        autor = input ("Introduzca el autor del libro: ")
        paginas = int(input ("Introduzca el numero de paginas del libro: "))
        genero = input ("Introduzca el genero del libro: ")

print(Libro)