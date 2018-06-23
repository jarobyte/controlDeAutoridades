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

archivo = "import/datos/prueba_registros.csv"
registros = pd.read_csv(archivo).values
print("el archivo " + archivo + " ha sido cargado...ES CORRECTO??")
print()

parser = argparse.ArgumentParser(description = "")
parser.add_argument('--first-range',
                    type = int,
                    nargs = 2)
parser.add_argument('--second-range',
                    type = int, 
                    nargs = 2)
args = parser.parse_args()
first_range = list(map(int, args.first_range))
second_range = list(map(int, args.second_range))

parejas = itertools.product(range(first_range[0],
                                  first_range[1]),
                            range(second_range[0],
                                  second_range[1]))
numero_de_parejas = int((first_range[1] - first_range[0])
                        * (second_range[1] - second_range[0]))
chunk_size = 10000
p = Pool()

resultado = [x for x in tqdm(p.imap_unordered(func = fun,
                                         iterable = parejas,
                                              chunksize = chunk_size),
                             total = numero_de_parejas) if x is not None]

with open("parejas.txt", 'w+') as archivo:
    archivo.write(str(resultado))
    archivo.write("\n")
