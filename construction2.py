from preprocesamiento_parejas import grouper
from deben_fusionarse.definiciones import deben_fusionarse
import pandas as pd
from multiprocessing import Pool
import itertools

def deb_fus(tupla):
    return deben_fusionarse(registros.iloc[tupla[0]],
                           registros.iloc[tupla[1]]), tupla

def procesarEnBloque(bloque):
    resultado = list(filter(deb_fus, bloque))
    return resultado


if __name__ == "__main__":
    registros = pd.read_csv("import/datos/prueba_registros.csv")
    parejas = itertools.combinations(range(registros.shape[0]), 2)
    
    p = Pool(2)
    res = [x for x in p.imap_unordered(deb_fus, parejas)]
    print(res)
    

#     block_size = 10
#     numero_de_bloque = int(0)
#     resultado_final = []

    
#     for bloque in grouper(parejas, block_size):
#         procesarEnBloque(bloque, resultado_final)
#         numero_de_bloque += 1
#     print("el resultado final es: "+ str(resultado_final))
