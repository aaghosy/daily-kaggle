#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np 
import pandas as pd 
df = pd.read_csv('C:/Users/logan/Documents/GitHub/daily-kaggle/kaggle playground/Titanic/source data/train.csv')


info = df.info()
missing = df.isnull().sum()
summary = df.describe(include='all').transpose()

(df.head(),missing,summary.head(15))


# In[ ]:




