#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

# In[6]:


from sklearn.datasets import load_iris

# In[2]:


vector = np.random.randint(0, 5, (2, 2))

# In[4]:


projected_vectors = np.random.randint(0, 1, (2, 2))

projected_vectors[0][0] = vector[0][0]
projected_vectors[1][1] = vector[1][1]

# In[5]:


projection_x_axis = (np.dot(vector[0], projected_vectors[0]) / np.dot(projected_vectors[0], projected_vectors[0])) * \
                    projected_vectors[0]
projection_y_axis = (np.dot(vector[0], projected_vectors[1]) / np.dot(projected_vectors[1], projected_vectors[1])) * \
                    projected_vectors[1]

# In[7]:


df = load_iris()

# In[8]:


eigen_values, eigen_vectors = np.linalg.eig(df['data'][:4])

# In[9]:


eigen_values, eigen_vectors

# In[14]:


import pandas as pd

df2 = pd.DataFrame(data=np.c_[df['data'], df['target']],
                   columns=df['feature_names'] + ['target'])
df2

# In[16]:


# ZERO Centralizing the DATA
mean_list = []
for i in df2.columns:
    mean_list.append(df2[i].mean())

for i, j in zip(df2.columns, mean_list):
    df2[i][:] -= j

# In[25]:


ecg = pd.read_csv(r"C:\Users\abdul\Desktop\ECG200_TRAIN.csv", delimiter="  ", header=None)
ecg

# In[26]:


# ZERO Centralizing the DATA
mean_list = []
for i in ecg.columns:
    mean_list.append(ecg[i].mean())

for i, j in zip(ecg.columns, mean_list):
    ecg[i][:] -= j

# In[27]:


ecg

# In[ ]:




