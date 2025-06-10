def mostrar_libros_disponibles(Listado):
    print("\nLos libros disponibles son:\n")
    lista_disponible =[]
    for libro in Listado:
        if libro["stock"]>0:
            print(f"{libro["titulo"]}, {libro["autor"]}")
            lista_disponible.append(libro)
    print("\n")
    print("Ingrese un rango de precios")
    precio_min = float(input("Precio mínimo: "))
    precio_max = float(input("Precio máximo: "))
    print("\nLos libros dentro de ese rango son:\n")
    for libro in lista_disponible:
        if libro["precio"]>= precio_min and libro["precio"]<= precio_max:
            print(f"{libro["titulo"]}, {libro["autor"]}")

    # def comprar_libros(Titulo, Cantidad):
    #     for 

lista_libros = [{"titulo":"General Relativity", "autor":"Robert M. Wald","precio":23530.,"stock":15},
                {"titulo":"Gravitation: foundations and Frontiers","autor":"Thanu Padmanabhan","precio":33945.,"stock":7},
                {"titulo":"Spacetime and Geometry","autor":"Sean Carroll","precio":19860.,"stock":1},
                {"titulo":"The Feynman Lectures on Physics", "autor":"Richard Feynman","precio":33720.,"stock":9},
                {"titulo":"The Large Scale Structure of Space-Time","autor":"Stephen Hawking","precio":15344.,"stock":0},
                {"titulo":"Introduction to the AdS/CFT Correspondence","autor":"Horaƫiu Năstase","precio":48814.,"stock":36}]

mostrar_libros_disponibles(lista_libros)
