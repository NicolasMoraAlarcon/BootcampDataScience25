import pandas as pd

# Entrada
sales = [100, 200, 1300, 400, 1500, 1801, 2000, 3000, 4000, 5000]
months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre']
s = pd.Series(sales, index=months)
print(s)