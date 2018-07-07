
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


def enviar_a_identificadores(tupla):
    persona = df[tupla[1]]
    identificador_CA = tupla[0]
    curps_persona = persona[:, [0,13,14]]
    cvus_persona = persona[:,[7,13,14]]
    orcids_persona = persona[:,[8,13,14]]
    rns_persona = persona[:,[9,13,14]]
    dni_persona = persona[:,[10,13,14]]
    identificadores = ([[identificador_CA] + ["curp"] + list(renglon) for renglon in curps_persona] + 
                   [[identificador_CA] + ["cvu"] + list(renglon) for renglon in cvus_persona] + 
                   [[identificador_CA] + ["orcid"] + list(renglon) for renglon in orcids_persona] + 
                   [[identificador_CA] + ["rn"] + list(renglon) for renglon in rns_persona])
    return identificadores


# In[12]:


enviar_a_identificadores(personas[2])


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
for i in list(p.map(enviar_a_identificadores, per)):
    final += i
final


# In[10]:


identificadores = pd.DataFrame(final, columns = ["identificador_CA", "tipo_de_identificador", "valor", "origen", "numero_de_registro"])


# In[11]:


identificadores


# In[14]:


identificadores.to_csv("identificadores.csv")

