import itertools

preposiciones = {"a", "ante", "bajo", "cabe", "con", "contra", "de",
                 "desde", "durante", "en", "entre", "hacia", "hasta",
                 "mediante", "para", "por", "según", "sin", "so", "sobre",
                 "tras", "versus", "vía"}

articulos = {"el", "la", "los", "las", "un", "unos", "una", "unas"}

conectivos = {"y"}

def difieren_por_letra_inicial(palabra1,palabra2):
    return ((palabra1[1:] == palabra2[1:]) & (palabra1 != palabra2))

def alguna_letra_inicial_diferente(lista_1, lista_2):
    if len(lista_1) == len(lista_2):
        for i in range(len(lista_1)):
            if (letra_inicial_diferente(lista_1[i], lista_2[i])
                & (lista_1[:i] == lista_2[:i])):
                return True

    return False

def aplicar_a_listas(lista_1, lista_2, funcion):
    contador = 0
    if len(lista_1) == len(lista_2):
        for i in range(len(lista_1)):
            if (funcion(lista_1[i], lista_2[i])
                & (suprimir_de_lista(lista_1, i)
                   == suprimir_de_lista(lista_2, i))):
                contador += 1
    return (contador > 0)

def suprimir_de_lista(lista, indice_del_elemento_a_suprimir):
    return [x for x in lista if x != lista[indice_del_elemento_a_suprimir]]

def difieren_por_letra_final(palabra1, palabra2):
    return ((palabra1[:-1] == palabra2[:-1]) & (palabra1 != palabra2))

def hay_abreviatura(palabra1, palabra2):
    return (((palabra1[-1] == ".") | (palabra2[-1] == "."))
            & (palabra1[0] == palabra2[0]))

def una_letra_faltante(palabra1, palabra2):
    if (len(palabra1) == len(palabra2) + 1):
        for i in range(len(palabra1)):
            if ((palabra1[0:i] == palabra2[0:i])
                & (palabra1[(i + 1):] == palabra2[i:])):
                return True
    return False

def letra_faltante(palabra1, palabra2):
    return (una_letra_faltante(palabra1, palabra2)
            | una_letra_faltante(palabra2, palabra1))

def letra_distinta(palabra1, palabra2):
    if (len(palabra1) == len(palabra2)):
        for i in range(len(palabra1)):
            if ((palabra1[0:i] == palabra2[0:i])
                & (palabra1[i + 1:] == palabra2[i + 1:])):
                return True
    return False
