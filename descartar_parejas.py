from progress.bar import Bar
import itertools
import pandas as pd
import deben_fusionarse.herramientas as h
import debe_descartarse as dd

registros = pd.read_csv("datos/registros.csv")
#numero_de_registros = registros.shape[0]
numero_de_registros = 17
combinaciones = (numero_de_registros - 1) * (numero_de_registros)/2
print("hay " + str(int(combinaciones)) + " combinaciones")


bar = Bar("Eliminando aristas obvias",
          max = combinaciones,
          suffix = "quedan %(remaining)d parejas")
          #suffix = "quedan %(remaining)d parejas por revisar, eta: %(eta)d seg")
parejas = itertools.combinations(range(numero_de_registros), 2)
lista_de_parejas = []
for i, j in parejas:
    registro_1 = registros.iloc[i]
    registro_2 = registros.iloc[j]
    if not dd.debe_descartarse(registro_1, registro_2):
        lista_de_parejas.append((i,j))
    
    bar.next()
bar.finish()
print(lista_de_parejas)
print(len(lista_de_parejas))
