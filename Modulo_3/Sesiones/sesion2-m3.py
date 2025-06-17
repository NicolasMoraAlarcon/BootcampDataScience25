import pandas as pd

datos = {"Jugador":["Lionel Messi", "Cristiano Ronaldo","Kevin De Bruyne","Kylian Mbappé","Luka Modric"],
                       "Posición":["Delantero","Delantero","Mediocampista","Delantero","Mediocampista"],
                       "Edad":[35,38,31,24,37],"Goles":[20,18,8,25,3],"Asistencias":[10,5,15,12,8]}

Datos = pd.DataFrame(datos)

print("\n",Datos["Jugador"],"\n")
print(Datos[["Jugador","Goles"]][Datos["Goles"]>10])
print("\n")
Datos["Puntos"] = Datos["Goles"]*4+Datos["Asistencias"]*2
print(Datos)
print(f"\nPromedio de goles = {Datos["Goles"].mean()}\n")
print(f"Máximo de asistencias = {Datos["Asistencias"].max()}\nMínimo de asistencias = {Datos["Asistencias"].min()}\n")
print(Datos["Posición"].value_counts(),"\n")
print(Datos.sort_values(by = "Goles",ascending=False),"\n")
print(Datos.describe())