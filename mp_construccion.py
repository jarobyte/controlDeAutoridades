import preprocesamiento_parejas as pp
import deben_fusionarse.lib as df
import pandas as pd
import itertools
import multiprocessing as mp



if __name__ == "__main__":
    registros = pd.read_csv("datos/registros.csv")
    parejas = itertools.combinations(range(registros.shape[0]), 2)
    block_size = 100
    numero_de_bloque = int(0)
    
    def deb_fus(tupla):
        return df.deben_fusionarse(registros.iloc[tupla[0]],
                               registros.iloc[tupla[1]])

    def procesarEnBloque(bloque):
        resultado = list(filter(deb_fus,bloque))
        print(resultado)
        print("bloque " + str(numero_de_bloque) + " completado")
        return resultado
    
    for bloque in pp.grouper(parejas, block_size):
        p = mp.Process(target = procesarEnBloque, args = ((bloque,)))
        p.start()
        numero_de_bloque += 1
