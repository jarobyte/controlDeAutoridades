import pandas as pd
import itertools
from multiprocessing import Pool
import construccion as c
from tqdm import tqdm
from deben_fusionarse.definiciones import existen_identificadores as function

def fun(tupla):
    if function(registros.iloc[tupla[0]],registros.iloc[tupla[1]]): return tupla
    return

registros = pd.read_csv("import/datos/prueba_registros.csv")
parejas = itertools.combinations(range(registros.shape[0]), 2)
numero_de_parejas = int((registros.shape[0]) * (registros.shape[0] - 1) / 2)
p = Pool()
#resultado = filter(p.imap_unordered(deb_fus, parejas))
resultado = [x for x in tqdm(p.imap_unordered(fun, parejas),
                             total = numero_de_parejas) if x != None]
print(resultado)
