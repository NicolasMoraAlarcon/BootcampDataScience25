import pandas as pd
import numpy as np

info = pd.read_csv("ventas4.csv")
print("Visualizar información:\n\n",info)

print("\nIdentificar valores perdidos\n\n",info.isnull())
print(info.isnull().sum(),"\n")
print("Falta un precio de categoría Moda, ingresamos el promedio de los precios de esa categoría")
moda = info[info["Categoría"]=="Moda"]
mean_moda = moda["Precio"].mean()
info.fillna({"Precio":mean_moda},inplace=True)
print("Los productos sin categoría se establecen como Desconocida\n")
info.fillna({"Categoría":"Desconocida"},inplace=True)
print(info,"\n")

print("Identificar duplicado\n\n",info.duplicated(),"\n")
info_sindup = info.drop_duplicates()
print("Sin duplicados\n\n",info_sindup)

Q1 = info_sindup["Cantidad"].quantile(0.25) 
Q3 = info_sindup["Cantidad"].quantile(0.75)
IQR = Q3 - Q1

info_sinoutliers = info_sindup[(info_sindup["Cantidad"]>=Q1-1.5*IQR)&((info_sindup["Cantidad"]<=Q3+1.5*IQR))]
print("\nInformación sin outliers\n","\n",info_sinoutliers)

print("\nModificar la estructura del DataFrame\n")
melted = pd.melt(info_sinoutliers,id_vars=["Cliente_ID","Nombre"],var_name="Información",value_name="Dato",value_vars=["Categoría","Cantidad","Precio","Método de Pago","Fecha"])
print(melted)

