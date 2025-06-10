# cont = 0
# while cont < 7:
#     print(f"{cont+1}, Hola")
#     cont +=1

#contando y paridad
# cont = 1
# while cont<= 13:
#     if cont%2==0:
#         print(f"Número {cont} es par")
#     else:
#         print(f"Número {cont} es impar")
#     cont += 1

# palabra = input("Ingrese una palabra")
# cont = 0
# while cont < len(palabra):
#     print(f"Letra en posición {cont}: {palabra[cont]}")
#     cont += 1

#menu while

# opcion = ""
# while opcion != "4":
#     print("1. suma")
#     print("2. resta")
#     print("3. multiplicacion")
#     print("4. Salir")
#     opcion = input("Seleccione una opción " )

#     if opcion == "1":
#         print("Has seleccionado la suma")
#         numero1 = float(input("ingrese el primer numero"))
#         numero2 = float(input("ingrese el segundo numero"))
#         print(f"La suma de {numero1} y {numero2} es {numero1+numero2}")
#     elif opcion == "2":
#         print("Has seleccionado la resta")
#         numero1 = float(input("ingrese el primer numero"))
#         numero2 = float(input("ingrese el segundo numero"))
#         print(f"La resta de {numero1} y {numero2} es {numero1-numero2}")
#     elif opcion == "3":
#         print("Has seleccionado la multiplicacion")
#         numero1 = float(input("ingrese el primer numero"))
#         numero2 = float(input("ingrese el segundo numero"))
#         print(f"La multiplicación de {numero1} y {numero2} es {numero1*numero2}")
#     elif opcion == "4":
#         print("Saliendo del programa")
#     else:
#         print("Opción inválida")

opcion = ""
numeros = input("Ingrese numeros separados por un espacio: ").split()
while opcion != "5" :
    print("1. Sumar los numeros")
    print("2. Calcular el promedio")
    print("3. Numeros mayor y menor")
    print("4. Ingresar nuevos numeros")
    print("5. Salir del programa")
    opcion = input("Ingrese una opción: ")
    if opcion == "1" or opcion == "2":
        suma = 0.
        for i in range(len(numeros)):
            suma = suma + float(numeros[i])
        if opcion == "1":
            print(f"La suma es {suma} \n")
        else:
            print(f"El promedio es {suma/len(numeros)} \n")
    elif opcion == "3":
        lista = []
        for x in numeros:
            lista.append(float(x))
        print(f"El número mayor es {max(lista)} y el número menor es {min(lista)} \n")
    elif opcion == "4":
        numeros = input("Ingrese los numeros: ").split()
    elif opcion =="5":
        print("Saliendo del programa")
    else:
        print("Opción inválida")
    

