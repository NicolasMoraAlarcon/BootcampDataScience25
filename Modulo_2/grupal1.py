# import random as rd

# #Equipo 1
# #1 Formato correo electrónico
# nombre = input("ingrese su nombre : ")
# dominio = input("ingrese su dominio, ej: gmail.com: ")
# correo = nombre+"@"+dominio
# print(correo)

# #2 contador de palabras
# frase = input("Ingrese una frase: ")
# palabras = frase.split()
# print(f"Su frase {frase} tiene {len(palabras)} palabras")
# print(palabras)

# #3 mensaje de invitación
# evento = input("Ingrese el nombre del evento: ")
# invitado = input("Ingrese el nombre de su invitado: ")
# print(f"¡Bienvenido a {evento}, {invitado}!")

# #Equipo2
# #1 generador de contraseña simple
# nombre = input("Ingrese su primer nombre: ")
# numero = input("Ingrese un número: ")
# simbolo = input("Ingrese un símbolo: ")
# password = nombre+numero+simbolo
# print(f"Su contraseña es {password}")

# #2 extracto iniciales
# nombre_completo = input("Ingrese su nombre completo: ").split()
# iniciales = [I[0] for I in nombre_completo]
# print(f"Sus iniciales son {iniciales}")

# #3 longitud nombre
# nombre = input("Ingrese su nombre y apellido: ").split()
# a = str("")
# for x in nombre:
#     a = a+x
# print(len(a))

# #Equipo 3
# #1 formateador de titulo
# titulo = input("Ingrese el título del libro: ")
# titulo_formateado = titulo.title()

# print(f"Título formateado es {titulo_formateado}")

# #2 reemplazo de texto
# frase = input("ingrese una frase a modificar: ").split()
# palabra = input("ingrese su palabra a reemplazar:")
# j = rd.randint(0,len(frase))
# nueva_frase = str("")
# for i in range(len(frase)):
#     if i==j:
#         nueva_frase = nueva_frase +' ' + palabra
#     else:
#         nueva_frase = nueva_frase + " " + frase[i]
# print(nueva_frase)

# #3 costo por letra 
# palabra = input("Ingrese una palabra: ")
# costo = input("Defina el coste ($) de una letra: ")
# costo_total = len(palabra)*float(costo)
# print(f"El costo de tu palabra es de ${costo_total}.")


# #Equipo 4
# #1
# nombre= input("Ingrese su nombre: ")
# prof = input("Ingrese su profesión: ")
# print(f"Hola {nombre} \n ¡Eres un gran {prof}!")
# #2
# palabra = input("ingrese una palabra: ").split()
# if len(palabra) == 0:
#     a = True
# else:
#     a = False
# print(f"El valor booleano es {a}")
# #3
# calle = input("Ingrese su calle: ")
# numero = input("Número: ")
# ciudad = input("y la ciudad donde vive: ")
# direccion = input("Ingrese su dirección, calle número y ciudad separados por un espacio: ").split()
# print(f"Su dirección es {calle} {numero}, {ciudad}")

# #Equipo 5
# #1 formateador de fecha
# fecha = input("Ingrese los números del día mes y año separados por un espacio: ").split()
# if int(fecha[0]) < 10:
#     fecha[0] ='0'+fecha[0]
# if int(fecha[1]) < 10:
#     fecha[1] ='0'+fecha[1]
# print(f"{fecha[0]}/{fecha[1]}/{fecha[2]}")

# #2 contador de espacios
# frase = input("Cuentame una frase y te diré cuantos espacios entre palabras hay: ")
# cont = 0
# for i in frase:
#     if i == ' ':
#         cont = cont + 1
# print(f"Hay {cont} espacios")

# #3 mensaje motivacional
# nombre = input("Ingrese su nombre: ")
# objetivo = input("Ingrese un pbjetivo personal: ")

# print(f"{nombre}, ¡tu puedes {objetivo}")

x = input("").split()
x = x[0]
# x.remove("k")
print(x)