#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import unittest
import sqlite3
import pandas as pd
from Extraction import by_date,by_product,by_customer,by_top_customers


# In[ ]:
class TestExtraction(unittest.TestCase):         #setUp and tearDown are default functions of unittest that gets called automatically
    def  setUp(self):
        self.conn=sqlite3.connect(":memory:")
        self.create_table()
        self.insert_data()
        self.df = self.to_df()

    def tearDown(self):
        self.conn.close()    
    def create_table(self):    #since we are running test cases in temporary memory , new create_table and insert_data functions are required 
        cursor = self.conn.cursor()
        table_command = """
            CREATE TABLE IF NOT EXISTS orders (
            order_id TEXT PRIMARY KEY,
            customer_id TEXT,
            order_date DATE,
            product_id TEXT,
            product_name TEXT,
            product_price REAL,
            quantity INTEGER
        );
        """
        cursor.execute(table_command)
        self.conn.commit()


    def insert_data(self):
        order=[('1', 'C001', '2023-01-01', 'P001', 'Product A', 253.50, 2),
            ('2', 'C002', '2023-02-15', 'P002', 'Product B', 459.00, 1),
            ('3', 'C001', '2023-03-20', 'P003', 'Product C', 7500.75, 3),
            ('4', 'C002', '2023-03-20', 'P001', 'Product B', 459.00, 3)]
        cursor = self.conn.cursor()
        insert_command = """
            INSERT INTO orders (order_id, customer_id, order_date, product_id, product_name, product_price, quantity)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """
        cursor.executemany(insert_command, order)
        self.conn.commit()
    def to_df(self):                        #df Dataframe is returned so that the functions imported from extraction could be used 
        select_query ="""select * from orders"""         #assertEqual functions checks that after the function call the generated value is equal to the distinct entires in dataset
        df=pd.read_sql_query(select_query,self.conn)
        return df 
    def test_monthly(self):
        monthly_revenue=by_date(self.df)
        print("Monthly Revenue:", monthly_revenue)
        self.assertEqual(len(monthly_revenue),3)
    def test_product(self):
        product_revenue=by_product(self.df)
        print("product_revenue:", product_revenue)
        self.assertEqual(len(product_revenue),3)
    def test_customer(self):
        customer_revenue=by_customer(self.df)
        print("customer_revenue", customer_revenue)
        self.assertEqual(len(customer_revenue),2)
    def test_by_top_consumer(self):
        top_customers=by_top_customers(self.df)
        print("top_customer", top_customers)
        self.assertEqual(len(top_customers),2)

