#!/usr/bin/env python
# coding: utf-8

# In[1]:

# same as extraction python file however no reading of the csv since it is a library for test.py and test does not require to read csv 
# it accepts the df Dataframe and returns the values 
import numpy as np
import pandas as pd


# In[19]


# In[26]:


def by_date(df):
    df['order_date']=pd.to_datetime(df['order_date'])
    df['year']=df['order_date'].dt.year
    df['month']=df['order_date'].dt.month
    df['revenue']=df['quantity']*df['product_price']
    monthly_revenue=df.groupby(['year','month'])['revenue'].sum().reset_index()
    monthly_revenue.columns=['Year','Month','Revenue']
    return monthly_revenue 



# In[31]:


def by_product(df):
    df['revenue']=df['quantity']*df['product_price']
    product_revenue=df.groupby(['product_id'])['revenue'].sum().reset_index()
    product_revenue.columns=['product_id','Revenue']
    return product_revenue



# In[32]:


def by_customer(df):
    df['revenue']=df['quantity']*df['product_price']
    customer_revenue=df.groupby(['customer_id'])['revenue'].sum().reset_index()
    customer_revenue.columns=['customer_id','Revenue']
    return  customer_revenue



# In[37]:
def by_top_customers(df):
    customer_revenue=by_customer(df)
    top_customers=customer_revenue.sort_values(by=['Revenue'],ascending=False).head(10)
    return top_customers



# In[ ]:




