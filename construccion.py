import preprocesamiento_parejas as pp
from deben_fusionarse.definiciones import deben_fusionarse
import pandas as pd
import itertools
import multiprocessing as mp



if __name__ == "__main__":
    registros = pd.read_csv("import/datos/prueba_registros.csv")
    parejas = itertools.combinations(range(registros.shape[0]), 2)
    block_size = 10
    numero_de_bloque = int(0)
    def deb_fus(tupla):
        return deben_fusionarse(registros.iloc[tupla[0]],
                               registros.iloc[tupla[1]])

    def procesarEnBloque(bloque):
        resultado = list(filter(deb_fus,bloque))
        print(resultado)
        print("bloque " + str(numero_de_bloque) + " completado")
        return resultado
    
    for bloque in pp.grouper(parejas, block_size):
        procesarEnBloque(bloque)
        numero_de_bloque += 1
