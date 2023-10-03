#!/usr/bin/env python
# coding: utf-8

# ## BRAZIL FOREST FIRE ANALYSIS
# PREPARED BY : ISHAN NAUTIYAL \
# DATE : 21/09/2023 \
# DATA : KAGGLE 

# In[2]:


# lets import the importatnt libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


# get the data and see the datattype of the data 
df1 = pd.read_csv("C:\\Users\\ishan\\datasets\\amazon.csv",encoding='iso-8859-1',parse_dates=['date'])


# In[4]:


df1=pd.DataFrame(df1)


# In[10]:


df1.head()


# In[11]:


df1.tail()


# In[12]:


df1.dtypes


# In[13]:


df1.shape


# In[14]:


df1.info()


# In[15]:


df1.describe(include='all')


# In[16]:


dup_data = df1.duplicated().any()


# In[17]:


dup_data


# In[18]:


df1= df1.drop_duplicates()


# In[19]:


df1.shape


# In[20]:


df1.isnull().sum()


# In[23]:


df1['month'].unique()


# In[33]:


df1['month_new']= df1['month'].map({'Janeiro':'jan','Fevereiro':'feb','Março':'mar','Abril':'apr','Maio':'may','Junho':'jun','Julho':'jul','Agosto':'ags','Setembro':'sep','Outubro':'oct','Novembro':'nov','Dezembro':'dec'})


# In[25]:


df1.head()


# In[26]:


df1.shape


# In[27]:


df1.columns


# In[30]:


data1= df1.groupby('month_new')['number'].sum().reset_index()


# In[31]:


data1


# In[34]:


sns.barplot(x='month_new',y='number',data=data1)
plt.figure(figsize=(16,5))
plt.show()


# In[37]:



data2= df1.groupby('year')['number'].sum().reset_index()


# In[38]:


data2


# In[39]:


plt.figure(figsize=(16,5))
sns.barplot(x='year',y='number',data=data2)


# In[5]:


data3 = df1.groupby('state')['number'].sum().sort_values(ascending=False).reset_index()


# In[6]:


data3


# In[12]:


plt.figure(figsize=(16,5))
plt.xticks(rotation=75)
sns.barplot(x='state',y='number',data=data3)


# In[15]:


data4=df1[df1['state']=='Amazonas']['number'].sum()


# In[18]:


data5=df1[df1['state']=='Amazonas']


# In[20]:


data6= data5.groupby('year')['number'].sum().reset_index()
data6


# In[23]:


plt.figure(figsize=(16,5))
plt.xticks(rotation=75)
plt.show()
sns.barplot(x='year',y='number',data=data6)


# In[24]:


df1.columns


# In[26]:


data7=df1.groupby('state')['number'].mean().sort_values(ascending=False).reset_index()
data7


# In[27]:


plt.figure(figsize=(16,5))
plt.xticks(rotation=75)
sns.barplot(x='state',y='number',data=data7)


# In[34]:


df1.columns


# In[35]:


data8=df1[df1['year']==2015]


# In[41]:


data8[data8.where(data8['month_new']=='dec').all(1)]['state']


# In[53]:


df1[df1.where(df1['month_new']=='dec').all(1)]

