import herramientas.lib as h
import pandas as pd
import re
import numpy

"""
Para cada una de las funciones, los parámetros 
registro_1
registro_2
deben de ser DataFrames de Pandas con una sola fila y las siguientes 
columnas:
['curp',
 'primer_apellido',
 'segundo_apellido',
 'nombres',
 'fecha_de_nacimiento',
 'pais_asociado',
 'genero',
 'cvu',
 'orcid',
 'rn',
 'dni',
 'pais_de_nacimiento',
 'afiliacion',
 'origen']
"""
def similitud_0(registro_1, registro_2):
    """El nombre es exactamente igual."""
    return ((registro_1["nombres"] == registro_2["nombres"]) 
            & (registro_1["primer_apellido"]
               == registro_2["primer_apellido"]) 
            & (registro_1["segundo_apellido"]
               == registro_2["segundo_apellido"]))

def similitud_1(registro_1, registro_2):
    """Diferencia entre acentos, guiones, diacríticos, artículos y 
    preposiciones."""
    palabras_prohibidas = (set(h.preposiciones)
                           | set(h.articulos)
                           | set(h.conectivos))
    nombre_1 = (re.split("-|\s",registro_1["nombres"])
                + re.split("-|\s",registro_1["primer_apellido"])
                + re.split("-|\s",registro_1["segundo_apellido"]))
    nombre_2 = (re.split("-|\s",registro_2["nombres"])
                + re.split("-|\s",registro_2["primer_apellido"])
                + re.split("-|\s",registro_2["segundo_apellido"]))
    return (set(nombre_1) ^ set(nombre_2) <= palabras_prohibidas)


def similitud_2(registro_1, registro_2):
    """1 letra sobrante o faltante 
    dentro de la palabra"""
    return ((h.letra_faltante(registro_1["nombres"], registro_2["nombres"])
             | (registro_1["nombres"] == registro_2["nombres"]))
            & 
            (h.letra_faltante(registro_1["primer_apellido"],
                              registro_2["primer_apellido"])
             | (registro_1["primer_apellido"]
                == registro_2["primer_apellido"])) 
            & 
            (h.letra_faltante(registro_1["segundo_apellido"],
                              registro_2["segundo_apellido"])
             | (registro_1["segundo_apellido"]
                == registro_2["segundo_apellido"])))
    
def similitud_3(registro_1, registro_2):
    """Letra inicial diferente en alguna de las partes del nombre"""
    funcion = h.difieren_por_letra_inicial
    return ((h.aplicar_a_listas(registro_1["nombres"].split(),
                                registro_2["nombres"].split(),
                                funcion))
            |(h.aplicar_a_listas(registro_1["primer_apellido"].split(),
                                 registro_2["primer_apellido"].split(),
                                 funcion))
            |(h.aplicar_a_listas(registro_1["segundo_apellido"].split(),
                                 registro_2["segundo_apellido"].split(),
                                 funcion)))

def similitud_4(registro_1, registro_2):
    """Última letra de la palabra diferente y las demás iguales"""
    funcion = h.difieren_por_letra_final
    return ((h.aplicar_a_listas(registro_1["nombres"].split(),
                                registro_2["nombres"].split(),
                                funcion))
            |(h.aplicar_a_listas(registro_1["primer_apellido"].split(),
                                 registro_2["primer_apellido"].split(),
                                 funcion))
            |(h.aplicar_a_listas(registro_1["segundo_apellido"].split(),
                                 registro_2["segundo_apellido"].split(),
                                 funcion)))
            
def similitud_5(registro_1, registro_2):
    """Hay abreviaturas"""
    funcion = h.hay_abreviatura
    return ((h.aplicar_a_listas(registro_1["nombres"].split(),
                                registro_2["nombres"].split(),
                                funcion))
            |(h.aplicar_a_listas(registro_1["primer_apellido"].split(),
                                 registro_2["primer_apellido"].split(),
                                 funcion))
            |(h.aplicar_a_listas(registro_1["segundo_apellido"].split(),
                                 registro_2["segundo_apellido"].split(),
                                 funcion)))

def similitud_6(registro_1, registro_2):
    """El campo de nombre de uno contiene dos o más elementos que otro."""
    return ((len(set(registro_1["nombres"].split())
                 & set(registro_2["nombres"].split()))
             == min(len(registro_1["nombres"].split()),
                    len(registro_2["nombres"].split())))
             & (registro_1["primer_apellido"]
                == registro_2["primer_apellido"])
             & (registro_1["segundo_apellido"]
                == registro_2["segundo_apellido"]))

def similitud_7(registro_1, registro_2):
    """El campo de nombre de uno contiene dos o más elementos distintos 
    al otro y los campos de apellido son iguales."""
    if ((len(registro_1["nombres"].split())
        == len(registro_2["nombres"].split()))
        & (registro_1["nombres"] != registro_2["nombres"])):
        return ((len(set(registro_1["nombres"].split())
                     & set(registro_2["nombres"].split()))
                 < len(registro_1["nombres"].split()))
                & (registro_1["primer_apellido"]
                   == registro_2["primer_apellido"])
                & (registro_1["segundo_apellido"]
                   == registro_2["segundo_apellido"]))
    return False

def similitud_8(registro_1, registro_2):
    """Si alguno de los campos es completamente diferente entre uno y 
    otro."""
    return (((registro_1["nombres"] != registro_2["nombres"])
             & (registro_1["primer_apellido"]
                == registro_2["primer_apellido"])
             & (registro_1["segundo_apellido"]
                == registro_2["segundo_apellido"]))
             | ((registro_1["nombres"] == registro_2["nombres"])
               & (registro_1["primer_apellido"]
                  != registro_2["primer_apellido"])
               & (registro_1["segundo_apellido"]
                  == registro_2["segundo_apellido"]))
             |((registro_1["nombres"] == registro_2["nombres"])
               & (registro_1["primer_apellido"]
                  == registro_2["primer_apellido"])
               & (registro_1["segundo_apellido"]
                  != registro_2["segundo_apellido"])))

def deben_fusionarse(registro_1, registro_2):
    if existen_identificadores(registro_1, registro_2):
        if existen_datos_auxiliares(registro_1, registro_2):
            if (similitud_0(registro_1, registro_2)
                or similitud_1(registro_1, registro_2)
                or similitud_2(registro_1, registro_2)
                or similitud_3(registro_1, registro_2)
                or similitud_4(registro_1, registro_2)
                or similitud_5(registro_1, registro_2)
                or similitud_6(registro_1, registro_2)
                or similitud_7(registro_1, registro_2)
                or similitud_8(registro_1, registro_2)):
                return True
    return False

def existen_identificadores(registro_1, registro_2):
    return ((registro_1["curp"] == registro_2["curp"])
            or (registro_1["cvu"] == registro_2["cvu"])
            or (registro_1["orcid"] == registro_2["orcid"])
            or (registro_1["rn"] == registro_2["rn"])
            or (registro_1["dni"] == registro_2["dni"]))

def existen_datos_auxiliares(registro_1, registro_2):
    return ((registro_1["pais_de_nacimiento"]
             == registro_2["pais_de_nacimiento"])
            or (registro_1["pais_asociado"]
                 == registro_2["pais_asociado"])
            or (registro_1["fecha_de_nacimiento"]
                 == registro_2["fecha_de_nacimiento"])
            or (registro_1["afiliacion"] == registro_2["afiliacion"])
            or (registro_1["genero"] == registro_2["genero"]))
