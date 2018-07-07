import pandas as pd
import multiprocessing as mp

with open("personas.txt", "r") as archivo:
    cadena = archivo.read()
lista = eval(cadena)
personas = list(enumerate(lista))

base = pd.read_csv("registros.csv")
df = base.values

def enviar_a_variantes_de_nombres(tupla):
    persona = df[tupla[1]]
    
    identificador_CA = tupla[0]
    nombres = persona[:,[3,1,2,13,14]]
    return [[identificador_CA] + list(renglon) for renglon in nombres]

per = personas
final = []
p = mp.Pool()
for i in list(p.map(enviar_a_variantes_de_nombres, per)):
    final += i
variantes_de_nombres = pd.DataFrame(final, columns = ["identificador_CA", 
                                                      "variante_de_nombre", 
                                                      "variante_de_primer_apellido",
                                                      "variante_de_segundo_apellido",
                                                      "origen",
                                                      "numero_de_registro"])
variantes_de_nombres.to_csv("variantes_de_nombres.csv")

