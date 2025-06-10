productos = ["libros","teclados","cuadernos","lapices","mouses"]
print(f"Los cinco productos son {productos}")
productos.append("pantallas")
productos.append("cargadores")
productos_destacados = productos[:3]
print("Ahora los productos son: ",productos,"\n",
      "Los productos destacados son: ",productos_destacados)
import random as rd
inventario = {x: len(x)*rd.randint(1,10)*7 for x in productos }
print("Nuestro inventario es", inventario)
inventario["planificador"] = rd.randint(5,300)
print("Se agrega el producto",list(inventario.keys())[-1])
print(inventario)
i = rd.randint(0,4)
item = list(inventario.keys())[i]
print(f"Del producto {item} hay {inventario[item]} artículos en stock")
categorias = ("electronico","librería","accesorios")
print(f"La segunda categoría es {categorias[1]}")
cat1, cat2, cat3 = categorias
productos_unicos = productos
for i in range(len(productos)):
    for j in range(len(productos)):
        if i!=j and productos[i]==productos[j]:
            productos_unicos.remove(productos[j])
if productos == productos_unicos:
    print("Se verifica que no hay elementos duplicados")
productos_mayusculas = [x.upper() for x in inventario]
print(productos_mayusculas)