#Calculadora de Perímetro de Rectángulo: 
# Haga un programa que solicite la base
#  y la altura de un rectángulo, calcule el perímetro (2 * base + 2 * altura), y muestre el resultado.

b = float(input("Ingrese la base del rectángulo: "))
a = float(input("Ingrese la altura del rectángulo: "))

print(f"El perímetro es {2*(a+b)}")

age = 20
country = "Chile"
if age >= 18 and country == "Chile":
    print("You must vote in Chile")
else:
    print("You couldn't vote in Chile")