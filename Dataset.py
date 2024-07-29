#!/usr/bin/env python
# coding: utf-8

# In[8]:


import sqlite3
import uuid
import random
import datetime
import pandas as pd


# In[5]:

# creating a generate function to generate a table orders that would serve as primary csv for our analysis
def generate(order_id,customer_id,order_date,product_id,product_name,product_price,quantity):
    conn=sqlite3.connect("Database.db")# establishing connection to database
    cursor=conn.cursor()# using cursor to navigate through database execution commands
    table_command="""
    Create Table IF NOT EXISTS orders(order_id Primary key,
    customer_id TEXT,
    order_date DATE,
    product_id TEXT,
    product_name varchar(20),
    product_price float,
    quantity Integer);
    """
    cursor.execute(table_command)# to execute the table command and establish a table orders in Database
    try: 
        order_id=order_id
        customer_id= customer_id
        order_date=  order_date
        product_id=   product_id
        product_name= product_name
        product_price=  product_price
        quantity=   quantity
        insert_command= """
        Insert INTO orders(order_id,customer_id, order_date,product_id,product_name,product_price,quantity)
        values(?,?,?,?,?,?,?)
        """
        with conn:                        #insert command is executed and the parameters to the cursor is provided in the form of tuple
            cursor.execute( insert_command,(order_id, customer_id, order_date, product_id, product_name, product_price, quantity))
            conn.commit()       #after the final set of update command , connection is asked to commit the changes 
    except sqlite3.Error as e:
        print("Error executing SQL:", e)
    finally:                                    #closing th cursor and the connection once the sql commands are finished 
        if cursor:                              #cursor close closes navigation through Database and connection close closes connection to database
            cursor.close()
        if conn:
            conn.close()
  
        


# In[6]:
# here an automation of data generation is done for the orders csv using the following function

products = [
    {"product_id": "P001", "product_name": "Product A", "product_price": 253.50},
    {"product_id": "P002", "product_name": "Product B", "product_price": 459.00},
    {"product_id": "P003", "product_name": "Product C", "product_price": 7500.75},
    {"product_id": "P004", "product_name": "Product D", "product_price": 152.25},
    {"product_id": "P005", "product_name": "Product E", "product_price": 501.00},
    {"product_id": "P006", "product_name": "Product F", "product_price": 9000.1},
    {"product_id": "P007", "product_name": "Product G", "product_price": 4500.00},
    {"product_id": "P008", "product_name": "Product H", "product_price": 7534.75},
    {"product_id": "P009", "product_name": "Product I", "product_price": 1500.25},
    {"product_id": "P0010", "product_name": "Product J", "product_price": 50000.00}
]
def generate_id():                 #function defined to generate unique ids that is for order and customer id 
    return str(uuid.uuid4())
def gen_product():                  #function is generate a random product entry from the products list provided the signature of product_id,product_name,product_price
    product=random.choice(products)
    return product["product_id"],product["product_name"],product["product_price"]
def gen_quant():                    #function to generate quantity of product randomly
    return random.randint(1,5)
def gen_order_date():               # function to generate date in the format of "%Y-%m-%d" by taking a start date and random days and concatenating to produce order date
    start_date = datetime.datetime.now() - datetime.timedelta(days=365)
    random_days = random.randint(0, 365)
    order_date = start_date + datetime.timedelta(days=random_days)
    return order_date.strftime("%Y-%m-%d")
for _ in range(0,2001):
    customer_id = generate_id()
    order_id = generate_id()
    order_date = gen_order_date()
    product_id, product_name, product_price = gen_product()
    quantity = gen_quant()
    generate(order_id, customer_id ,order_date,product_id,product_name,product_price ,quantity)
print("Success")


# In[10]:


conn=sqlite3.connect("Database.db")
select_query="""
Select* from orders
"""
df=pd.read_sql_query(select_query,conn)
conn.close()
df.to_csv("orders.csv",index=False)
print("Saved")
    


# In[ ]:




