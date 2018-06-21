from preprocesamiento_parejas import grouper
from deben_fusionarse.definiciones import deben_fusionarse
import pandas as pd
import itertools

def deb_fus(tupla):
    return deben_fusionarse(registros.iloc[tupla[0]],
                           registros.iloc[tupla[1]])

def procesarEnBloque(bloque, lista_para_registrar):
    resultado = list(filter(deb_fus,bloque))
    lista_para_registrar += resultado
    print("bloque " + str(numero_de_bloque) + " completado")
    return

if __name__ == "__main__":
    registros = pd.read_csv("import/datos/prueba_registros.csv")
    parejas = itertools.combinations(range(registros.shape[0]), 2)
    block_size = 10
    numero_de_bloque = int(0)
    resultado_final = []

    
    for bloque in grouper(parejas, block_size):
        procesarEnBloque(bloque, resultado_final)
        numero_de_bloque += 1
    print("el resultado final es: "+ str(resultado_final))
