with open("personas_final.txt", "r") as archivo:
    cadena = archivo.read()
lista = eval(cadena)
personas = list(enumerate(lista))

import pandas as pd
base = pd.read_csv("import/datos/registros.csv")
df = base.values

columnas_registro_principal = ["identificador_CA", 
                                "nombre_completo",
                                "primer_apellido_completo", 
                                "segundo_apellido_completo", 
                                "nombre_preferido", 
                                "primer_apellido_preferido", 
                                "segundo_apellido_preferido", 
                                "lugar_de_nacimiento",
                                "institucion",
                                "afiliacion",
                                "genero", 
                                "fecha_de_nacimiento",
                                "estado_de_identificacion"]
registro_principal = pd.DataFrame(columns = columnas_registro_principal)

columnas_variantes_de_nombres = ["identificador_CA", 
                                               "nombres", 
                                               "primer_apellido", 
                                               "segundo_apellido"]
variantes_de_nombres = pd.DataFrame(columns = columnas_variantes_de_nombres)

columnas_identificadores = ["identificador_CA", "tipo", "valor"]
identificadores = pd.DataFrame(columns = columnas_identificadores)

def extraer_dato(persona, columna, lista_de_prioridades):
    dato = ""
    mini_base = persona[:,[13, columna]]
    for renglon in mini_base:
        if renglon[0] == lista_de_prioridades[0]:
            if str(renglon[1]) != "nan":
                dato = renglon[1]
                return dato
    for renglon in mini_base:
        if renglon[0] == lista_de_prioridades[1]:
            if str(renglon[1]) != "nan":
                dato = renglon[1]
                return dato
    for renglon in mini_base:
        if renglon[0] == lista_de_prioridades[2]:
            if str(renglon[1]) != "nan":
                dato = renglon[1]
                return dato
    return dato

def enviar_a_registro_principal(tupla):
    persona = df[[tupla[1]]]
    
    indicador_CA = tupla[0]
    nombre_completo = extraer_dato(persona, 3, ["cvu", "rn", "dape"])
    primer_apellido_completo = extraer_dato(persona, 1, ["cvu", "rn", "dape"])
    segundo_apellido_completo = extraer_dato(persona, 2, ["cvu", "rn", "dape"])
    nombre_preferido = extraer_dato(persona, 3, ["rn", "dape", "cvu"])
    primer_apellido_preferido = extraer_dato(persona, 1, ["rn", "dape", "cvu"])
    segundo_apellido_preferido = extraer_dato(persona, 2, ["rn", "dape", "cvu"])
    lugar_de_nacimiento = extraer_dato(persona, 11, ["cvu", "dape", ""])
    institucion = extraer_dato(persona, 12, ["rn", "", ""])
    if institucion != "":
        afiliacion = "Actual"
    else:
        afiliacion = ""
    genero = extraer_dato(persona, 6, ["cvu", "", ""])
    fecha_de_nacimiento = extraer_dato(persona, 4, ["cvu", "dape", ""])
    if len(persona) == 1:
        estado_de_identificacion = "preliminar"
    else:
        estado_de_identificacion = "preliminar fusionado"
    
    datos =[indicador_CA, 
            nombre_completo, 
            primer_apellido_completo, 
            segundo_apellido_completo, 
            nombre_preferido, 
            primer_apellido_preferido,
            segundo_apellido_preferido,
            lugar_de_nacimiento, 
            institucion,
            afiliacion,
            genero,
            fecha_de_nacimiento,
            estado_de_identificacion]
    return datos

import multiprocessing as mp

p = mp.Pool()
per = personas
array = p.map(func = enviar_a_registro_principal, iterable = iter(per))
reg_prin = pd.DataFrame(array, columns = columnas_registro_principal)
reg_prin.to_csv("rp.csv")

