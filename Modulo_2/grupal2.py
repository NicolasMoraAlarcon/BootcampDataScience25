# opcion = ""
# lista = [float(x) for x in range(-10,10)]
# # print(lista)
# while opcion != "5":
#     print("Menu:")
#     print("1. Agregar un numero a la litsa")
#     print("2. Ver la lista completa")
#     print("3. Ver solo los numeros pares")
#     print("4. Ver solo los numeros impares")
#     print("5. Salir del programa")
#     opcion = input("Escoja una opción: ")
#     if opcion == "1":
#         lista.append(float(input("Ingrese el numero que desea agregar ")))
#     elif opcion == "2":
#         print(lista)
#     elif opcion == "3" or opcion == "4":
#         par = []
#         impar = []
#         for x in lista:
#             if x%2==0.:
#                 par.append(x)
#             else:
#                 impar.append(x)
#         if opcion == "3":
#             print(par)
#         else:
#             print(impar)
#     elif opcion == "5":
#         print("Saliendo del programa")
#     else:
#         print("Opcion incorrecta")
#############################################################
# frutas = ("manzana", "frutilla", "platano", "naranja","manzana","sandia","platano","pera","manzana")
# lista_fruta = []
# opcion = ''
# while opcion != "5":
#     print("Menu:")
#     print("1. Ver todas las frutas")
#     print("2. Contar cuantas veces aparece una fruta específica")
#     print("3. Agregar una fruta")
#     print("4. Mostrar inventario actualizado")
#     print("5. Salir del programa")
#     opcion = input("Escoja una opción: ")
#     if opcion == "1":
#         for x in frutas:
#             print(x)
#     elif opcion == "2":
#         fruta = input("Escriba la fruta que quiere revisar: ").lower()
#         cont = 0
#         for x in frutas:
#             if fruta == x:
#                 cont += 1
#         print(f"La fruta {fruta} aparece {cont} veces")
#     elif opcion == "3":
#         for x in frutas:
#             lista_fruta.append(x)
#         fruta = input("Escriba la fruta que quiere agregar: ")
#         lista_fruta.append(fruta)
#     elif opcion == "4":
#         if len(lista_fruta) == 0:
#             for x in frutas:
#                 print(x)
#         else:
#             for x in lista_fruta:
#                 print(x)
#     elif opcion == "5":
#         print("Saliendo del programa")
#     else:
#         print("Opcion incorrecta") 


# estudiantes = { "estudiante1" : {
#     "nombre": "Cristian", ""
# } 



# }


Rutas = { "ruta 1" : {"nombre" : "roja", "distancia" : "10 km", "tarifa base": "$500", "vehiculo" : "bus"},
          "ruta 2" : {"nombre" : "amarilla","distancia" : "7 km", "tarifa base": "$450", "vehiculo" : "taxi"},
          "ruta 3" : {"nombre" : "azul","distancia" : "5 km", "tarifa base": "$250", "vehiculo" : "bus"},
          "ruta 4" : {"nombre" : "verde","distancia" : "12 km", "tarifa base": "$750", "vehiculo" : "taxi"}
}
opcion = ""
while opcion != "5":
    print("MENU:")
    print("1. AGREGUE RUTA: NOMBRE DISTANCIA TARIFA_BASE VEHICULO")
    print("2. BUSCAR RUTA POR TIPO DE VEHICULO")
    print("3. CALCULAR TARIFA AJUSTADA DE LA RUTA: ")
    print("4. ELIMINAR RUTAS CON DISTANCIA INFERIOR A:")
    print("5. ADIÓS")
    # if opcion == "1":
    opcion = input("SELECCIONE UNA OPCION ")
    auto = ""
    if opcion == "2":
        auto = input("ESCOJA BUS O TAXI: ").lower()
        nombre = []
        distancia = []
        tarifa = []
        for Ruta, datos in Rutas.items():
            if datos["vehiculo"]== auto: # and auto == "bus":
                nombre.append(datos["nombre"])
                distancia.append(datos["distancia"])
                tarifa.append(datos["tarifa base"])
            else:
                print("INGRESE BUS O TAXI")
        if len(nombre)>0:
            for i in range(len(nombre)):
                print(f"{nombre[i]}, {distancia[i]}, {tarifa[i]}")        
    elif opcion == "3":
        print("LAS RUTAS DISPONIBLES SON:")
        for Ruta, datos in Rutas.items():
            print(datos["nombre"])
        ruta = input("INDIQUE EL NOMBRE DE LA RUTA: ").lower()
        factor = float(input("INDIQUE EL FACTOR DE AJUSTE: "))
        for Ruta, datos in Rutas.items():
            if datos["nombre"]== ruta:
                tarifa = float(datos["tarifa base"].split()[0][1::])
                print(f"La tarifa ajustada es ${tarifa*factor} para la ruta {ruta}")
            else:
                print("SELECCIONES UN RUTA DISPONIBLE")
                break

