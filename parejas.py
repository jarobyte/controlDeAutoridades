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

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)

base_de_datos = "import/datos/prueba_registros.csv"
registros = pd.read_csv(base_de_datos).values
print("el archivo " + base_de_datos + " ha sido cargado...ES CORRECTO??")
if __name__ == '__main__':


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

    chunk_size = 5
    p = Pool()

    resultado = list(itertools.chain.from_iterable(tqdm(p.imap_unordered(func = list,
                                                                         iterable = [filter(fun,x) for x in grouper(parejas, chunk_size)],),
                                                        total = numero_de_parejas/chunk_size)))

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
