import pandas as pd
import itertools
from multiprocessing import Pool
from tqdm import tqdm
from deben_fusionarse.definiciones import existen_identificadores as function
import argparse

def fun(tupla):
    if function(registros[tupla[0]],registros[tupla[1]]):
        return tupla
    return

base_de_datos = "import/datos/registros.csv"
registros = pd.read_csv(base_de_datos).values
print("el archivo " + base_de_datos + " ha sido cargado...ES CORRECTO??")

parser = argparse.ArgumentParser(description = "")
parser.add_argument('--inicio',
                    type = int,
                    default = 0)
parser.add_argument('--final',
                    type = int, 
                    default = registros.shape[0])
args = parser.parse_args()
inicio = int(args.inicio)
final = int(args.final)

numero_de_registros = final - inicio 
parejas = itertools.combinations(range(inicio, final), 2)
numero_de_parejas = int((numero_de_registros) * (numero_de_registros - 1) / 2)

chunk_size = 10000
p = Pool()

resultado = [x for x in tqdm(p.imap_unordered(func = fun,
                                              iterable = parejas,
                                              chunksize = chunk_size),
                             total = numero_de_parejas) if x is not None]


ruta_de_salida = ("resultados/"
        + "parejas--"
        + base_de_datos.replace("/","_")
        + "--("
        + str(inicio)
        + "-"
        + str(final)
        + ")x"
        + "("
        + str(inicio)
        + "-"
        + str(final)
        + ")")
with open(file = ruta_de_salida,
          mode = 'w+') as archivo:
    archivo.write(str(resultado))
    archivo.write("\n")
    
print("resultados registrados en:" + ruta_de_salida)
