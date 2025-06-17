import numpy as np
# tensor_3d = np.arange(1,25).reshape(2,3,4)
# print(tensor_3d,tensor_3d.ndim,tensor_3d.shape,tensor_3d.size
#       ,tensor_3d.size,tensor_3d.dtype)

# arreglo = np.arange(10,51,5)
# puntos = np.linspace(0,10,6)
# print(arreglo)
# print(puntos)

# matriz_cero = np.zeros((4,4))
# matriz_uno = np.ones((4,4))
# matriz_aleatoria = np.random.rand(4,4)
# matriz_identidad = np.eye(4)

# print(matriz_cero,matriz_cero,matriz_aleatoria,matriz_identidad)

matriz = np.array([[5,10,15],[20,25,30],[35,40,45]])
elemento = matriz[1,2]
segunda_fila = matriz[1,:]
print(elemento, segunda_fila)

mayor_que_20 = matriz[(20<matriz)&(matriz<40)]
cantidad_mayores_que_20 = mayor_que_20.size
cantidad = len(mayor_que_20)
print(mayor_que_20,cantidad_mayores_que_20,cantidad)