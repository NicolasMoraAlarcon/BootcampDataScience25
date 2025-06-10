# numero = int(input("Ingrese un numero: "))
# if numero % 2 ==0:
#     print("El numero es par")
# else:
#     print("El número es impar")

# if numero > 0:
#     print("El número es positivo")
# else:
#     print("El número es negativo")

# #verificar usuario y contraseña
# usuario = input("ingrese su usuario: ")
# contrasena = input("Ingrese su contraseña")

# if usuario == "admin" and  contrasena == "1234":
#     print("Acceso concedido")
# else:
#     print("Acceso denegado")

# capital = input("Ingrese la capital de Chile: ")
# if capital.lower() == "santiago":
#     print(f"La capital de Chile es Santiago")
# else:
#     print(f"{capital} no es la capital de Chile")

# calificacion = int(input("Ingrese su calificacion: "))
# if calificacion > 100 or calificacion < 0:
#     print("Calificacion invalida")
# else:
#     if calificacion >= 90:
#         print("A")
#     elif calificacion >= 80:
#         print("B")
#     elif calificacion >= 70:
#         print("C")   
#     elif calificacion >= 60:
#         print("D")  
#     else:
#         print("F")   


edad = int(input("Ingrese su edad: "))
if edad<0 or edad >120:
    print("Ingrese una edad mayor a cero años y menor a 120 años")
else:
    if edad >0 and edad <= 12:
        print("Usted es niño/a")
    elif edad >12 and edad <= 17:
        print("Usted es adolescente")
    elif edad >17 and edad <= 59:
        print("Usted es adulto/a")
    elif edad >59:
        print("Usted es adulto/a mayor")
