import pandas as pd
import itertools
import multiprocessing as mp
import construccion as c
from preprocesamiento_parejas import grouper

c.registros = pd.read_csv("import/datos/registros.csv")
parejas = itertools.combinations(range(c.registros.shape[0]), 2)
block_size = 10000
c.numero_de_bloque = int(0)
resultado_final = []

for bloque in grouper(parejas, block_size):
    p = mp.Process(target = c.procesarEnBloque, args = ((bloque,
                                                         resultado_final)))
    p.start()
    c.numero_de_bloque += 1
