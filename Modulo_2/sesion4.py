def calcular_area_rectangulo(largo, ancho):
    return largo*ancho
import math as m
def calcular_circunferencia(radio):
    return 2*m.pi*radio
def calcular_promedio(lista_de_numeros):
    nota = 0.
    for i in lista_de_numeros:
        nota = nota + i
    return nota/len(lista_de_numeros)
import statistics as st
def calcular_promedio_avanzado(lista_de_numeros):
    return st.mean(lista_de_numeros)
import random as rd
def generar_numeros_aleatorios(cantidad, limite):
    lista = []
    for i in range(cantidad):
        lista.append(rd.randint(1, limite))
    return lista