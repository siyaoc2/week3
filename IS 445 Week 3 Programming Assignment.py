#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams["font.family"] = "sans-serif"


# In[3]:


games = pd.read_csv('https://data.illinois.gov/dataset/2c47ae63-3be1-4985-904b-c5e5f4bf79ee/resource/aa78b062-07b2-40b4-8e24-e23778fa2f01/download/data.csv')


# In[4]:


games


# In[5]:


games["zip_code"].min()#Find the lowest zip code


# In[6]:


games.loc[games["total_ticket_sales"] < 60000] #List all entries with a sales amount lower than 60000


# In[7]:


#Find the sales amounts and their corresponding zip codes for first 20 entries in the file
games_entries = pd.read_csv('https://data.illinois.gov/dataset/2c47ae63-3be1-4985-904b-c5e5f4bf79ee/resource/aa78b062-07b2-40b4-8e24-e23778fa2f01/download/data.csv', nrows=20)


# In[8]:


games_entries


# In[42]:


with plt.style.context("seaborn"):
    ax = games_entries.plot(x = "zip_code", y= "total_ticket_sales", figsize=(8,6), linewidth = 5.0, kind ="bar" ,color = "#ff007f")
    plt.show


# I chose to utilize a bar chart as a visualization to reveal the relationship between the variables "zip_code" and "total_ticket_sales" in the horizontal and vertical axis. This is because the bar chart enables me to see the trend and the correlation between the variables' values. In other words, it is easy to compare among datasets, such as the various ticket sale amount between the zipcode of 60002 and 60004. However, I dislike this type of visualization is the limitations associated with that; for example, a bar chart can only be applied for just two variables. Moreover, it isn't easy to be read accurately. 
