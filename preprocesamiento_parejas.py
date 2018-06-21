import itertools
import pandas as pd
import multiprocessing as mp



def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)

def escribir_en_archivo(nombre_del_archivo, bloque_de_tuplas):
    print(nombre_del_archivo)
    with open(file = nombre_del_archivo, mode = "w+") as archivo:
        for tupla in bloque_de_tuplas:
            archivo.write(str(tupla))
            archivo.write("\n")
    return

if __name__ == "__main__":
    registros = pd.read_csv("datos/registros.csv")
    parejas = itertools.combinations(range(registros.shape[0]), 2)
    block_size = 100000
    #parejas = itertools.combinations(range(10),2)
    #block_size = 5

    numero_de_archivo = int(0)
    for bloque in grouper(parejas, block_size):
        archivo_cadena = "agrupar_parejas/parejas" + str(numero_de_archivo) + ".txt"
        p = mp.Process(target = escribir_en_archivo, args = (archivo_cadena,
                                                             bloque))
        p.start()
        numero_de_archivo += 1
