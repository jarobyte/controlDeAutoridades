
# coding: utf-8

# In[1]:


from deben_fusionarse import definiciones as d


# In[2]:


import pandas as pd


# In[3]:


registros = pd.read_csv("import/datos/registros.csv").fillna("")


# In[4]:


registros.fillna("")


# In[5]:


r = registros.values


# In[1]:


with open("aristas.txt", "r") as archivo:
    aristas = eval(archivo.read())


# In[2]:


aristas[0]


# In[ ]:


def f(tupla):
    return d.deben_fusionarse(r[tupla[0]], r[tupla[1]])


# In[ ]:


f(aristas[0])


# In[ ]:



