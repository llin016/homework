#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


df =pd.read_excel(r"C:\Users\llin1\OneDrive\Desktop\USvideos.xlsx")
df


# In[3]:


df=df.drop_duplicates()
df


# In[5]:


df.dtypes


# In[4]:


df=df.drop(columns =['title','channel_title','tags','comments_disabled','ratings_disabled','video_error_or_removed','description'])
df


# In[6]:


df.dtypes


# In[9]:


df = df.set_index('views')
df


# In[10]:


df.isna().sum()


# In[11]:


df.describe()


# In[14]:


df.hist(bins=40,figsize=(20,10))


# In[15]:


pd.DataFrame(df['category_id'].value_counts())


# In[16]:


pd.DataFrame(df['publish_time'].value_counts())


# In[20]:


pd.DataFrame(df['publish_time'].value_counts()).plot(kind='bar',figsize=(20,15))


# In[3]:





# In[ ]:




