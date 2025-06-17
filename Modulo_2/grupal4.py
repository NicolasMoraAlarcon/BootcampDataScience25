import math as m
import statistics as stats

def distancia_haversine(Latitud_1,Longitud_1,Latitud_2,Longitud_2):
    La1= m.radians(Latitud_1)
    Lo1 = m.radians(Longitud_1)
    La2 = m.radians(Latitud_2)
    Lo2 = m.radians(Longitud_2)
    r = 6371 #km
    d = 2*r*m.asin(m.sqrt(m.sin((La2-La1)/2)**2+m.cos(La1)*m.cos(La2)*m.sin((Lo2-Lo1)/2)**2))
    return print(round(d,2))

lat1, lon1 = 19.43, -99.13 #Ciudad de México
lat2, lon2 = 4.71, -74.07 # Bogotá
print("Distancia Haversine")
distancia_haversine(lat1,lon1,lat2,lon2)


########## Yacimiento #########
def evaluar_yacimiento(Porosidades, Radio):
    for P in Porosidades:
        if P >0. and P<1.:
            True
        else:
            print("Ingrese porosidades entre 0 y 1")
            return 0
    phi = stats.mean(Porosidades)
    h = 100
    Volumen = m.pi*Radio**2*h*phi
    return print({'porosidad_media':round(phi,2),"volumen":round(Volumen,2)})

porosidades = [0.1,0.15,0.2]
radio = 5
print("Evaluación yacimiento")
evaluar_yacimiento(porosidades,radio)

#promedio calificaciones escolares

def promedio_calificaciones(Calificaciones):
    if len(Calificaciones)>0:
        True
    else:
        print("Ingrese calificaciones")
        return 0
    promedio = round(stats.mean(Calificaciones),2)
    if promedio>= 6.0:
        print(f"Promedio: {promedio}, Grupo: Aprobado")
    else:
        print(f"Promedio: {promedio}, Grupo: Reprobado")

calificaciones = [7.5,8.0,5.5,6.5]
promedio_calificaciones(calificaciones)


#Planificación de cursos

def planificar_cursos(N_est,Capacidades_maximas):
    for n in Capacidades_maximas:
        if n >0:            
            True
        else:
            print("Ingrese capacidades máximas positivas")
            return 0
    capacidad_promedio = stats.mean(Capacidades_maximas)
    N_cursos = m.ceil(N_est/capacidad_promedio)
    return print({"Capacidad promedio":round(capacidad_promedio),"cursos":round(N_cursos)})

estudiantes = 50
capacidades = [15,20,25]
print("Planificación cursos")
planificar_cursos(estudiantes,capacidades)



#################
import numpy as np

inventario = np.zeros((5,4))

for i in range(5):
    inventario[i] = np.random.randint(10,101,4)
    n = np.random.randint(0,4,1)[0]
    print("n vale",n)
    inventario[i][n] = np.random.randint(1,11,1) 
print("Inventario")
print(inventario)
