class PublicVehicle:
    def __init__(self,ID_vehiculo):
        self.ID_vehiculo = ID_vehiculo
        self.paradas_visitadas = []
    
    def visit_stop(self,stop):
        self.paradas_visitadas.append(stop)

    def stop_count(self):
        return len(self.paradas_visitadas[0])
    
def distance_estimate(stops): 
    dist = 0
    for stop in stops:
        dist += float(stop)
    return dist

while True:
    opcion1 = input("¿Agrega un nuevo vehículo? Si/No ").lower()
    if opcion1 == "si":
        id = PublicVehicle(input("Ingrese Id: "))
        paradas = input("Ingrese las paradas separadas por comas (,)").split(",")
        distancias = input("Ingrese las distancias separadas por (,)").split(",")
        for i in paradas:
            id.visit_stop(i)
        print(f"En {id.stop_count()} paradas recorre {distance_estimate(distancias)} km")
        print(id.paradas_visitadas)
    else:
        break
    
