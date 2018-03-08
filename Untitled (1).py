
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[20]:


import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("whitegrid")
get_ipython().run_line_magic('matplotlib', 'inline')


# In[45]:


df = pd.read_csv('data/nominas.csv', index_col='NUMERO DE EMPLEADO')
df.head(5)
df.iloc[:,8:20].head(5)

