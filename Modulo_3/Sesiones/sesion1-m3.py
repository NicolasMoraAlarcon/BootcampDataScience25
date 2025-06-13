import numpy as np #1

vec = np.arange(1,10.1) #2
print(vec)

matriz = np.random.rand(3,3) #3
print(matriz)

identidad = np.eye(4) #4
print(identidad)

vec2 = np.reshape(vec,(2,5)) #5
print(vec2)

print("Mayores a 5",vec[vec>5]) #6

arr1 = np.arange(0,41,10) #7
arr2 = np.arange(20,161,30)
print("arreglo 1 =",arr1)
print("arreglo 2 =",arr2)
print("total =    ",arr1+arr2)

print("Raiz cuadrada",np.sqrt(vec)) #8
print("Exponencial",np.exp(vec))
print("Logaritmo 10",np.log10(vec))