class Libro:
    def __init__(self, titulo, autor, isbn):
        self.__titulo = titulo
        self.__autor = autor
        self.__isbn = isbn
    def get_titulo(self):
        return self.__titulo
    def get_autor(self):
        return self.__autor
    def get_isbn(self):
        return self.__isbn
    def descripcion(self):
        return f"Título: {self.__titulo}, Autor: {self.__autor}, ISBN: {self.__isbn}"

class Biblioteca:
    def __init__(self,biblioteca=[]):
        self.biblioteca = biblioteca
    def agregar_libro(self,libronuevo):
        self.biblioteca.append(libronuevo)
    def mostrar_libro(self):
        for i in self.biblioteca:
            print(i.descripcion())

libro1 = Libro("Física para ciencias e ingeniería","Renisck and Halliday","9788840807768")
libro2 = Libro("Classical Electrodynamics",'Jackson',"9780471309321")

biblio = Biblioteca()
biblio.agregar_libro(libro1)
biblio.agregar_libro(libro2)

biblio.mostrar_libro()
opcion = ''
while opcion != "no":
    opcion = input("¿Quiere agregar un libro? Si o No ").lower()
    if opcion == "si":
        a = input("Ingrese el título: ")
        b = input("Ingrese autor(es): ")
        c = input("Ingrese ISBN: ")
        libro = Libro(a,b,c)
        biblio.agregar_libro(libro)
    else:
        print("Saliendo de biblioteca...")
print("Sus libros son:")
biblio.mostrar_libro()

        