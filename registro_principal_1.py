
# coding: utf-8

# In[1]:


with open("personas.txt", "r") as archivo:
    cadena = archivo.read()


# In[2]:


lista = eval(cadena)


# In[3]:


personas = list(enumerate(lista))


# In[4]:


len(personas)


# In[24]:


per = personas
per


# In[6]:


import pandas as pd


# In[7]:


base = pd.read_csv("registros.csv")


# In[8]:


df = base.values


# In[9]:


df[[0, 10]]


# In[10]:


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
registro_principal


# In[11]:


columnas_variantes_de_nombres = ["identificador_CA", 
                                               "nombres", 
                                               "primer_apellido", 
                                               "segundo_apellido"]
variantes_de_nombres = pd.DataFrame(columns = columnas_variantes_de_nombres)
variantes_de_nombres


# In[12]:


columnas_identificadores = ["identificador_CA", "tipo", "valor"]
identificadores = pd.DataFrame(columns = columnas_identificadores)
identificadores


# In[13]:


def extraer_dato(persona, columnas, lista_de_prioridades):
    dato = ""
    
    mini_base = persona[:,[13] + columnas]
    for renglon in mini_base:
        if renglon[0] == lista_de_prioridades[0]:
            if str(renglon[1]) != "nan":
                dato = renglon[1:]
                return dato
    for renglon in mini_base:
        if renglon[0] == lista_de_prioridades[1]:
            if str(renglon[1]) != "nan":
                dato = renglon[1:]
                return dato
    for renglon in mini_base:
        if renglon[0] == lista_de_prioridades[2]:
            if str(renglon[1]) != "nan":
                dato = renglon[1:]
                return dato
    return dato


# In[14]:


list(enumerate(base))


# In[15]:


list(enumerate(columnas_registro_principal))


# In[20]:


def enviar_a_registro_principal(tupla):
    persona = df[[tupla[1]]]
    
    indicador_CA = tupla[0]
    nombre_completo = extraer_dato(persona, [3,1,2], ["cvu", "rn", "dape"])
#     primer_apellido_completo = extraer_dato(persona, [1], ["cvu", "rn", "dape"])
#     segundo_apellido_completo = extraer_dato(persona, [2], ["cvu", "rn", "dape"])
    nombre_preferido = extraer_dato(persona, [3,1,2], ["rn", "dape", "cvu"])
#     primer_apellido_preferido = extraer_dato(persona, [1], ["rn", "dape", "cvu"])
#     segundo_apellido_preferido = extraer_dato(persona, [2], ["rn", "dape", "cvu"])
    lugar_de_nacimiento = extraer_dato(persona, [11], ["cvu", "dape", ""])
    institucion = extraer_dato(persona, [12], ["rn", "", ""])
    if institucion != "":
        afiliacion = "Actual"
    else:
        afiliacion = ""
    genero = extraer_dato(persona, [6], ["cvu", "", ""])
    fecha_de_nacimiento = extraer_dato(persona, [4], ["cvu", "dape", ""])
    if len(persona) == 1:
        estado_de_identificacion = "preliminar"
    else:
        estado_de_identificacion = "preliminar fusionado"
    
    datos =[indicador_CA, 
            nombre_completo[0], nombre_completo[1], nombre_completo[2], 
#             primer_apellido_completo, 
#             segundo_apellido_completo, 
            nombre_preferido[0], nombre_preferido[1], nombre_preferido[2] ,
#             primer_apellido_preferido,
#             segundo_apellido_preferido,
            lugar_de_nacimiento, 
            institucion,
            afiliacion,
            genero,
            fecha_de_nacimiento,
            estado_de_identificacion]
    return datos


# In[21]:


import multiprocessing as mp


# In[22]:


p = mp.Pool()


# In[26]:


rp = pd.DataFrame(list(map(enviar_a_registro_principal,per)), columns = columnas_registro_principal)
rp


# In[27]:


rp.to_csv("rp.csv")


# In[ ]:


tupla = per[0]
persona = df[[tupla[1]]]
persona


# In[ ]:


nombre_completo = extraer_dato(persona, [3,1,2], ["cvu", "rn", "dape"])
nombre_completo


# In[ ]:


columnas = [3,1,2]
lista_de_prioridades = ["cvu", "rn", "dape"]


# In[ ]:


dato = ""
    
mini_base = persona[:,[13] + columnas]
mini_base


# In[ ]:


for renglon in mini_base:
    if renglon[0] == lista_de_prioridades[0]:
        if str(renglon[1]) != "nan":
            dato = renglon[1:]
            print(dato)
for renglon in mini_base:
    if renglon[0] == lista_de_prioridades[1]:
        if str(renglon[1]) != "nan":
            dato = renglon[1:]
            print(dato)
for renglon in mini_base:
    if renglon[0] == lista_de_prioridades[2]:
        if str(renglon[1]) != "nan":
            dato = renglon[1:]
            print(dato)


# In[ ]:


dato[0]

