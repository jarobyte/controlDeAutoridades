
# coding: utf-8

# In[1]:


import pandas as pd
import multiprocessing as mp


# In[2]:


with open("personas.txt", "r") as archivo:
    cadena = archivo.read()
lista = eval(cadena)
personas = list(enumerate(lista))


# In[3]:


base = pd.read_csv("registros.csv")
df = base.values


# In[4]:


def enviar_a_instituciones(tupla):
    persona = df[tupla[1]]
    
    identificador_CA = tupla[0]
    afiliaciones = persona[:, [12,13]]

    instituciones = ([[identificador_CA] + list(renglon) for renglon in afiliaciones])
    return instituciones


# In[12]:


enviar_a_instituciones(personas[2])


# In[13]:


personas[2]


# In[6]:


tupla = personas[0]
persona = df[tupla[1]]
identificador_CA = tupla[0]
curps_persona = persona[:, [0,13]]
cvus_persona = persona[:,[7,13]]
orcids_persona = persona[:,[8,13]]
rns_persona = persona[:,[9,13]]
dni_persona = persona[:,[10,13]]
[[identificador_CA] + list(renglon) for renglon in curps_persona]
identificadores = ([[identificador_CA] + ["curp"] + list(renglon) for renglon in curps_persona] + 
                   [[identificador_CA] + ["cvu"] + list(renglon) for renglon in cvus_persona] + 
                   [[identificador_CA] + ["orcid"] + list(renglon) for renglon in orcids_persona] + 
                   [[identificador_CA] + ["rn"] + list(renglon) for renglon in rns_persona])
identificadores


# In[7]:


per = personas
final = []
p = mp.Pool()
for i in list(p.map(enviar_a_instituciones, per)):
    final += i
final


# In[10]:


instituciones = pd.DataFrame(final, columns = ["identificador_CA", "institucion", "origen"])


# In[11]:


instituciones


# In[14]:


instituciones.to_csv("instituciones.csv")

