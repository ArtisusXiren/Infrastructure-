#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[19]:


df=pd.read_csv("orders.csv")


# In[26]:


def by_date():
    df['order_date']=pd.to_datetime(df['order_date'])
    df['year']=df['order_date'].dt.year
    df['month']=df['order_date'].dt.month
    df['revenue']=df['quantity']*df['product_price']
    monthly_revenue=df.groupby(['year','month'])['revenue'].sum().reset_index()
    monthly_revenue.columns=['Year','Month','Revenue']
    return monthly_revenue 
monthly_revenue=by_date()
print(monthly_revenue)


# In[31]:


def by_product():
    df['revenue']=df['quantity']*df['product_price']
    product_revenue=df.groupby(['product_id'])['revenue'].sum().reset_index()
    product_revenue.columns=['product_id','Revenue']
    return product_revenue
product_revenue=by_product()
print(product_revenue)


# In[32]:


def by_customer():
    df['revenue']=df['quantity']*df['product_price']
    customer_revenue=df.groupby(['customer_id'])['revenue'].sum().reset_index()
    customer_revenue.columns=['customer_id','Revenue']
    return customer_revenue
customer_revenue=by_customer()
print(customer_revenue)


# In[37]:
def by_top_customers():
    top_customers=customer_revenue.sort_values(by=['Revenue'],ascending=False).head(10)
    return top_customers
top_customers= by_top_customers()
print(top_customers)

# In[ ]:




