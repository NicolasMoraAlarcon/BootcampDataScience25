import pandas as pd

ventas = pd.read_csv("ventas.csv",sep=",")
print(ventas.head(),"\n")
for col in ventas.columns:
    if col[0] ==' ':
        ventas = ventas.rename(columns={col:col[1::]})
ven1 =ventas[["Producto","Precio"]]
print(ven1,"\n")

ven2 = ventas[ventas["Precio"]>50] 
print(ven2)

ven2.to_csv("ventas_mayor_50.csv",index=False)