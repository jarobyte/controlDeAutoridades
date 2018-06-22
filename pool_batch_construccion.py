import pandas as pd
import itertools
from multiprocessing import Pool
import construccion as c
from tqdm import tqdm
from deben_fusionarse.definiciones import existen_identificadores as function

def fun(tupla):
    if function(registros.iloc[tupla[0]],registros.iloc[tupla[1]]): return tupla
    return

def fun_filt(batch):
    return list(filter(fun, batch))

registros = pd.read_csv("import/datos/registros.csv")
parejas = itertools.combinations(range(registros.shape[0]), 2)
numero_de_parejas = int((registros.shape[0]) * (registros.shape[0] - 1) / 2)
chunk_size = 10000
p = Pool()
resultado = [x for x in tqdm(p.imap_unordered(func = fun,
                                         iterable = parejas,
                                              chunksize = chunk_size),
                             total = numero_de_parejas / chunk_size) if x!= None]

with open("parejas.txt", 'w+') as archivo:
    for i in resultado:
        archivo.write(str(i))
        archivo.write("\n")
