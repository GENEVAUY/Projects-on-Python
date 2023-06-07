#!/usr/bin/env python
# coding: utf-8

# Challenge 2: Structuring Data In this challenge, we will continue to work with customer data from an insurance company, but we will use a dataset with more columns, called marketing_customer_analysis.csv, which can be found at the following link:
# https://raw.githubusercontent.com/data-bootcamp-v4/data/main/marketing_customer_analysis.csv
# This dataset contains information such as customer demographics, policy details, vehicle information, and the customer's response to the last marketing campaign. Our goal is to explore and analyze this data by performing data cleaning, formatting, and structuring.
# Exercise 1: Clean and Format the Data While the dataset has been partially cleaned and formatted, we still need to perform several data cleaning tasks. Specifically, we need to standardize the column names, clean null values, convert the effective_to_date column to datetime, and extract the months from the dataset and store them in a separate column.
# To accomplish these tasks, we will use the functions created in the previous step to standardize the column names and deal with null values, and then we will apply additional functions to convert the effective_to_date column to datetime and extract the months.
# Save the clean dataset into a csv file.

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv ("https://raw.githubusercontent.com/data-bootcamp-v4/data/main/marketing_customer_analysis.csv")


# In[3]:


df


# In[4]:


df= df.rename(columns=str.lower)


# In[5]:


def rename_columns(df):
    df.rename (columns = {'effective to date':'datetime'}, inplace=True)
    return df

df = rename_columns(df)
df


# In[6]:


df.drop('unnamed: 0', axis=1, inplace=True)


# In[7]:


df = df.reset_index(drop=True)
df


# In[8]:


df.isna().sum()


# In[9]:


df = df.dropna(subset = "vehicle type")


# In[10]:


df = df.reset_index(drop=True)


# In[11]:


df.isna().sum()


# In[12]:


df = df.dropna(subset = "response")


# In[13]:


df = df.reset_index(drop=True)


# In[14]:


df.isna().sum()


# In[15]:


df = df.dropna(subset = "number of open complaints")


# In[16]:


df = df.reset_index(drop=True)


# In[17]:


df.isna().sum()


# In[18]:


mode_value1 = df['vehicle class'].mode()[0]


# In[19]:


df['vehicle class'].fillna(mode_value1, inplace=True)


# In[20]:


df.isna().sum()


# In[21]:


mode_value2 = df['vehicle size'].mode()[0]


# In[22]:


df['vehicle size'].fillna(mode_value2, inplace=True)


# In[23]:


df.isna().sum()


# In[24]:


#df['datetime'] = pd.to_datetime(df['datetime'])


# In[25]:


#df['month'] = df['datetime'].dt.month
#df


# In[26]:


df


# In[27]:


df


# In[28]:


df['datetime'] = pd.to_datetime(df['datetime'], format='%m/%d/%y')


# In[29]:


df['month'] = df['datetime'].dt.strftime('%m')


# In[30]:


df['datetime'] = df['datetime'].dt.strftime('%m/%d/%y')


# In[31]:


df

