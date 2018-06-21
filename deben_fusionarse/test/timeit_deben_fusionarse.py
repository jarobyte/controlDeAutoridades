from timeit import default_timer
from deben_fusionarse.definiciones import deben_fusionarse
from deben_fusionarse.definiciones import existen_identificadores
import pandas as pd

print("cargando archivo")
registros = pd.read_csv("import/datos/prueba_registros.csv")
registro_1 = registros.iloc[0]
registro_2 = registros.iloc[2]

start = default_timer()

print(deben_fusionarse(registro_1, registro_2))

mid = default_timer()

print(mid - start)

print(existen_identificadores(registro_1, registro_2))

end = default_timer()

print(end - mid)
