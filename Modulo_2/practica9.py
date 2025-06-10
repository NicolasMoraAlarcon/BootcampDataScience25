# number = [1,2,3,4,5,6,7,8,9,10]
# even_number = []
# for i in number :
#     if i%2 == 0:
#         even_number.append(i)
# print("Los números pares son:", even_number)

# letters = ['a','b','c','d','e']
# reversed_letters = reversed(letters)
# revers = []
# for i in range(len(letters)):
#     revers.append(letters[-1-i])

# print(reversed_letters)
# print(revers)

# numbers2 = [1,2,4,5,7,8,9,2,7,3,6,7,3,7,3,7,2,5]
# unique_numbers = []
# for i in numbers2:
#     if i not in unique_numbers:
#         unique_numbers.append(i)
# print(unique_numbers)

# coordenadas = [(122,467),(56,78),(12,45)]
# for punto in coordenadas:
#     print(f"coordenada: {punto[0]},{punto[1]}")
# coordenadas.append((10,20))


#set o conjuntos
# frutas = {"appel","banana","cherry", "date", "elderberry"}
# print(frutas)
# A={5,10,15,20,25}
# B = {10,20,30,40,50}
# print("union",A|B)
# A.add(35)
# print("A=",A)
# B.remove(30)
# print("interseccion",A&B)
# print("diferencia",A-B)
# print("diferencia simetrica",A^B)
# print("A es un subconjunto de B:", A.issubset(B))
# print("B es un superconjunto de A:",B.issuperset(A))
# print("A es disjunto de B:", A.isdisjoint(B))
# for x in A:
#     print(x)
# for i in range(len(A)):
#     print(A[i])

usuarios = {
    "usuario1": {
        "nombre": "Juan",
        "edad": 30,
        "ciudad": "Madrid",
    },
    "usuario2": {
        "nombre": "Ana",
        "edad": 25,
        "ciudad": "Barcelona",
    },
    "usuario3": {
        "nombre": "Luis",
        "edad": 35,
        "ciudad": "Valencia",
    },
}
#print(usuarios.items())
edades = []
for usarios, datos in usuarios.items():
    # print(datos["edad"])
    edades.append(datos["edad"])
promedio = sum(edades)/len(edades)
print(f"El promedio de edad es {promedio}")

#     print(f"{usuario.edad}")
#     promedio_edad = sum(edad) / len(usuario)
# print(f"promedio de edad: {promedio_edad}")  