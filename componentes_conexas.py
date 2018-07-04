
# coding: utf-8

# In[2]:


get_ipython().system('{"ls resultados/ -Rl"}')


# In[3]:


parejas = set()


# In[4]:


len(parejas)


# In[5]:


with open("resultados/gamma/parejas--import_datos_registros.csv--(0-100000)x(1200000-1700555)", "r") as archivo:
    cadena = archivo.read()
parejas = parejas | set(eval(cadena))
len(parejas)


# In[6]:


with open("resultados/gamma/parejas--import_datos_registros.csv--(100000-200000)x(1200000-1700555)", "r") as archivo:
    cadena = archivo.read()
parejas = parejas| set(eval(cadena))
len(parejas)


# In[7]:


with open("resultados/gamma/parejas--import_datos_registros.csv--(200000-300000)x(1200000-1700555)", "r") as archivo:
    cadena = archivo.read()
parejas = parejas | set(eval(cadena))
len(parejas)


# In[8]:


with open("resultados/gamma/parejas--import_datos_registros.csv--(300000-400000)x(1200000-1700555)", "r") as archivo:
    cadena = archivo.read()
parejas = parejas | set(eval(cadena))
len(parejas)


# In[9]:


with open("resultados/gamma/parejas--import_datos_registros.csv--(400000-500000)x(1200000-1700555)", "r") as archivo:
    cadena = archivo.read()
parejas = parejas | set(eval(cadena))
len(parejas)


# In[10]:


with open("resultados/meta-nodos/parejas--import_datos_registros.csv--(0-600000)x(0-600000)", "r") as archivo:
    cadena = archivo.read()
parejas = parejas | set(eval(cadena))
len(parejas)


# In[11]:


with open("resultados/meta-nodos/parejas--import_datos_registros.csv--(1200000-1700555)x(1200000-1700555)", "r") as archivo:
    cadena = archivo.read()
parejas = parejas | set(eval(cadena))
len(parejas)


# In[12]:


import pandas as pd


# In[13]:


df = pd.read_csv("import/datos/registros.csv")


# In[14]:


import networkx as nx


# In[15]:


G = nx.Graph()


# In[16]:


G.add_nodes_from(list(range(df.shape[0])))


# In[17]:


G.add_edges_from(parejas)

