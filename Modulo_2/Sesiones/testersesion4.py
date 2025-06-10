import sesion4 as s4

def tester(l1,l2,r,cant,maximo):
    area_rect = s4.calcular_area_rectangulo(l1,l2)
    area_circ = s4.calcular_circunferencia(r)
    L = s4.generar_numeros_aleatorios(cant,maximo)
    promedio = s4.calcular_promedio(L)
    promedio_avanzado = s4.calcular_promedio_avanzado(L)
    return print("El área del rectángulo es ",area_rect,"\n",
                 "El área del círculo es ",area_circ,"\n",
                 "La lista de números aleatorios es",L,"\n",
                 "El promedio es ", promedio,"\n",
                 "El promedio avanzado es ",promedio_avanzado)

tester(float(input("Ingrese el largo del rectángulo ")),
       float(input("Ingrese el ancho del rectángulo ")),
       float(input("Ingrese el radio del círculo ")),
       int(input("Ingrese la cantidad de números aleatorios ")),
       int(input("Ingrese el valor máximo de los números aleatorios ")) 
       )