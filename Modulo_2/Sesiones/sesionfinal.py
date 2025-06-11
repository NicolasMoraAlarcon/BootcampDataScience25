lista_libros = [{"titulo":"General Relativity", "autor":"Robert M. Wald","precio":23530.,"stock":15},
                {"titulo":"Gravitation: foundations and Frontiers","autor":"Thanu Padmanabhan","precio":33945.,"stock":7},
                {"titulo":"Spacetime and Geometry","autor":"Sean Carroll","precio":19860.,"stock":1},
                {"titulo":"The Feynman Lectures on Physics", "autor":"Richard Feynman","precio":33720.,"stock":9},
                {"titulo":"The Large Scale Structure of Space-Time","autor":"Stephen Hawking","precio":15344.,"stock":0},
                {"titulo":"Introduction to the AdS/CFT Correspondence","autor":"Horaƫiu Năstase","precio":48814.,"stock":36}]

descuentos = [{"autor":"Richard Feynman","%":35},
            {"autor":"Sean Carroll","%":50},
            {"autor":"Robert M. Wald", "%":20}]

def mostrar_libros_disponibles():
    Listado = lista_libros
    print("\nLos libros disponibles son:\n")
    lista_disponible =[]
    for libro in Listado:
        if libro["stock"]>0:
            print(f"{libro["titulo"]}, {libro["autor"]}")
            lista_disponible.append(libro)
    opcion = input("\n¿Desea filtrar por rango de precio? Si/No ").lower()
    if opcion == "si":
        print("Ingrese un rango de precios")
        precio_min = float(input("Precio mínimo: "))
        precio_max = float(input("Precio máximo: "))
        print("\nLos libros dentro de ese rango son:\n")
        for libro in lista_disponible:
            if libro["precio"]>= precio_min and libro["precio"]<= precio_max:
                print(f"{libro["titulo"]}, {libro["autor"]}, ${libro["precio"]}, stock:{libro["stock"]}")

def comprar_libros(Titulo, Cantidad):
    Listado = lista_libros
    Descuentos = descuentos
    Cantidad = int(Cantidad)
    for libro in Listado:
        if Titulo.lower() == libro["titulo"].lower():
            print("Libro está en inventario")
            if Cantidad <= libro["stock"]:
                print(f"Stock de {Cantidad} libros disponible")
                libro["stock"] = libro["stock"] - Cantidad
                costo = libro["precio"]*Cantidad
                ahorro = 0
                for desc in Descuentos:
                    if libro["autor"]==desc["autor"]:
                        ahorro = costo*float(desc["%"])/100.
                        costo = costo - ahorro
                        return costo , ahorro
            else:
                print(f"Stock insuficiente, quedan {libro["stock"]} unidades")
                return 0. , 0.
    return 0.,0.

def factura(Compras,Copias,Precio_total,Precio_ahorrado):
    for i in range(len(Compras)):
        print(f"{Compras[i]} x {Copias[i]} = ${Precio_total[i]}")
        print(f"Ahorro {100-int(round(Precio_total[i]/(Precio_total[i]+Precio_ahorrado[i])*100,2))}%: ${Precio_ahorrado[i]}")
    return sum(Precio_total)

mostrar_libros_disponibles()
opcion = ''
precio_final = 0
precio_ahorrado = 0
compras = []
copias = []
costos = []
ahorros = []
while opcion != "no":
    opcion = input("\n¿Desea agregar un libro a su compra? Si/No ").lower()
    if opcion == "si":
        a = input("\nTitulo que desea comprar: ")
        b = input("Cantidad que desea comprar: ")
        compras.append(a)
        copias.append(b)
        c,d = comprar_libros(a.lower(),b)
        costos.append(c)
        ahorros.append(d)
    elif opcion == "no":
        print("Finalizando compra\n")
    else:
        print("Opción incorrecta\n")


print(f"El precio a pagar es ${factura(compras,copias,costos,ahorros)}")
