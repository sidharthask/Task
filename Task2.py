#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


data=pd.ExcelFile(r"D:\task_output.xlsx")


# In[3]:


data


# In[4]:


df1=pd.read_excel(data, 'DEPOSITS')


# In[5]:


df2=pd.read_excel(data, 'WITHDRAWALS')


# In[6]:


df3=pd.read_excel(data, 'INSIGHTS')


# In[7]:


z=df1.append(df2)


# In[8]:


date=z.DATE


# In[9]:


date


# In[10]:


amount=z.AMOUNT


# In[11]:


amount


# In[12]:


ph_num=df3.iloc[1:3]


# In[13]:


ph_num


# In[14]:


mini=amount.min()


# In[15]:


mini


# In[16]:


maxi=amount.max()


# In[17]:


maxi


# In[18]:


deposite=df1


# In[20]:


deposite


# In[21]:


withdrawals=df2


# In[22]:


withdrawals


# In[ ]:




