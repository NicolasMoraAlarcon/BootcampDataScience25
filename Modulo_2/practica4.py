capital_inicial = float(input("Ingrese el monto de su capital inicial: "))
tasa_interes = float(input("Ingrese la tasa de interés anual: "))
años = int(input("Ingrese los años: "))

int_simple = capital_inicial*tasa_interes*años/100.
print(f"Su nuevo capital con interés simple después de {años} años es {int_simple}")

int_comp = capital_inicial*(1+tasa_interes/100.)**años
print(f"Su nuevo capital con interés compuesto después de {años} años es {int_comp}")