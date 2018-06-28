import pandas as pd
import itertools
from multiprocessing import Pool
from tqdm import tqdm
import parejas as par
import argparse

#base_de_datos = "import/datos/prueba_registros.csv"
#registros = pd.read_csv(base_de_datos).values
#print("el archivo " + base_de_datos + " ha sido cargado...ES CORRECTO??")

parser = argparse.ArgumentParser(description = "")
parser.add_argument('--primer-rango',
                    type = int,
                    nargs = 2)
parser.add_argument('--segundo-rango',
                    type = int, 
                    nargs = 2)
args = parser.parse_args()
primer_rango = list(map(int, args.primer_rango))
segundo_rango = list(map(int, args.segundo_rango))

parejas = itertools.product(range(primer_rango[0],
                                  primer_rango[1]),
                            range(segundo_rango[0],
                                  segundo_rango[1]))
numero_de_parejas = int((primer_rango[1] - primer_rango[0])
                        * (segundo_rango[1] - segundo_rango[0]))
chunk_size = 5
p = Pool()

# resultado = [x for x in tqdm(p.imap_unordered(func = par.fun,
#                                               iterable = parejas,
#                                               chunksize = chunk_size),
#                              total = numero_de_parejas) if x is not None]

resultado = list(itertools.chain.from_iterable(tqdm(p.imap_unordered(func = list,
                                                                     iterable = [filter(par.fun,x) for x in par.grouper(parejas, chunk_size)]),
                                                total = numero_de_parejas/chunk_size)))


ruta_de_salida = ("resultados/"
        + "parejas--"
        + par.base_de_datos.replace("/","_")
        + "--("
        + str(primer_rango[0])
        + "-"
        + str(primer_rango[1])
        + ")x"
        + "("
        + str(segundo_rango[0])
        + "-"
        + str(segundo_rango[1])
        + ")")
with open(file = ruta_de_salida,
          mode = 'w+') as archivo:
    archivo.write(str(resultado))
    archivo.write("\n")
print("resultados registrados en:" + ruta_de_salida)
