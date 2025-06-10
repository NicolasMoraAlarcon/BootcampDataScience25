#Requerimiento 1

print('Ingrese nombre del estudiantes y su calificación')
estudiante = {"nombre": input("Nombre del estudiante: \n"), "nota": float(input("Calificación: \n"))}

if estudiante['nota'] >= 60:
    print("Aprobó")
else:
    print("No aprobó")

#Requirimientos 2-6
lista = []
agregar = True
while agregar == True:
    print('Ingrese nombre del estudiantes y sus calificaciones en matemáticas, ciencias e inglés')
    persona = {"nombre": input("Nombre del estudiante: \n"), "nota_mate": float(input("Calificación de matemáticas: \n")),
           "nota_ciencias": float(input("Calificación de ciencias: \n")),"nota_ingles": float(input("Calificación de inglés: \n"))}
    persona["nota_promedio"] = (persona["nota_mate"]+persona["nota_ciencias"]+persona["nota_ingles"])/3

    if persona["nota_promedio"] >= 90.:
        #print("Su promedio de notas es Excelente")
        persona["eval"] =  "Excelente"
    elif persona["nota_promedio"] < 90. and persona["nota_promedio"] >= 75.:
        #print("Su promedio de notas Bueno")
        persona["eval"] =  "Bueno"
    else:
        #print("Su promedio de notas Necesita mejorar")
        persona["eval"]= "Necesita mejorar"
    persona["congrats"] = "¡Puntuación perfecta!" if persona["nota_promedio"]==100 else persona["eval"]
    #lista.append([persona["nombre"],persona["promedio"]])
    lista.append(persona)
    agregar = input("¿Desea agregar información de otro estudiante?. Si o No. ")

    if agregar == "Si" or agregar == "si":
        agregar = True
    else:
        agregar = False
for i in lista:
    if i["congrats"] == i["eval"]: 
        print(i["nombre"],":",i["eval"])
    else:
        print(i["nombre"],":",i["eval"],i["congrats"])


