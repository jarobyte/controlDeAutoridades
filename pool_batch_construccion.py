import pandas as pd
import itertools
from multiprocessing import Pool
import construccion as c
from tqdm import tqdm
from deben_fusionarse.definiciones import existen_identificadores as function
import argparse

def fun(tupla):
    if function(registros[tupla[0]],registros[tupla[1]]):
        return tupla
    return

def fun_filt(batch):
    return list(filter(fun, batch))

registros = pd.read_csv("import/datos/prueba_registros.csv").values
parser = argparse.ArgumentParser(description = "")
parser.add_argument('--lower_limit',
                    type = int,
                    default = 0)
parser.add_argument('--upper_limit',
                    type = int, 
                    default = registros.shape[0])
args = parser.parse_args()
lower_limit = int(args.lower_limit)
upper_limit = int(args.upper_limit)
numero_de_registros = upper_limit - lower_limit 
parejas = itertools.combinations(range(lower_limit, upper_limit), 2)
numero_de_parejas = int((numero_de_registros) * (numero_de_registros - 1) / 2)
chunk_size = 10000
p = Pool()

resultado = [x for x in tqdm(p.imap_unordered(func = fun,
                                         iterable = parejas,
                                              chunksize = chunk_size),
                             total = numero_de_parejas) if x is not None]

with open("parejas.txt", 'w+') as archivo:
    archivo.write(str(resultado))
    archivo.write("\n")
