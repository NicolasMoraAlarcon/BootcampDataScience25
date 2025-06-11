class Estudiante:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula

    def Presentarse(self):
        print(f"Mi nombre es {self.nombre} y mi matrícula es {self.matricula}")

#estudiante = Estudiante(input("¿Cuál es tu nombre? "),input("¿Cuál es tu matrícula? "))
#estudiante.Presentarse()

class Robot:
    def __init__(self, nombre, modelo):
        self.nombre = nombre #oublica
        self._modelo = modelo #protegido
        self.__energia = 100 #privada

    def obtener_modelo(self):
        return self._modelo
    
    def obtener_energia(self):
        return self.__energia
    def mostrar_info(self):
        print(f"Robot: {self.nombre}, Modelo: {self._modelo}, Energía: {self.__energia}")

robot1 = Robot("Robo1", "XJ-9")
print(robot1.nombre) #acceso publico
print(robot1.obtener_modelo()) #acceso protegido con un metodo
print(robot1.obtener_energia()) #acceso privado con un metodo
robot1.mostrar_info()
print("protegido",robot1._modelo)
print(robot1.__energia)