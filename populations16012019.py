
# coding: utf-8

# In[12]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_table('populations.txt')

year = data['# year']
heare = data['hare']
plt.plot(year, data['hare'])

