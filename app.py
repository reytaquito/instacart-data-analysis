import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
import time

df_orders = pd.read_csv('instacart_orders (1).csv', sep=';')
df_products = pd.read_csv('products.csv', sep=';')
df_aisles = pd.read_csv('aisles.csv', sep=';')
df_departments = pd.read_csv('departments.csv', sep=';')
df_order_products = pd.read_csv('order_products.csv', sep=';')

#clean data
df_orders.drop_duplicates(inplace=True)
df_orders.reset_index(drop=True, inplace=True)
df_products['product_name'].isna().sum()
df_products['product_name'] = df_products['product_name'].fillna('unknown')
df_order_products['add_to_cart_order'] = df_order_products['add_to_cart_order'].fillna(999) #fill with 999
df_order_products['add_to_cart_order'] = df_order_products['add_to_cart_order'].astype(int) #float to int


st.markdown("<h1 style='text-align: center;'>Instacart data analysis</h1>", unsafe_allow_html=True)
st.divider()

description = '''This project was created as a personal learning tool to help me explore and understand the various functionalities that Streamlit offers. By working on this project, I aim to gain hands-on experience with different components, data visualization techniques, and interactive features that Streamlit provides. My goal is to build a solid foundation so that in the future, I can efficiently implement Streamlit in more complex applications, whether for data analysis, interactive dashboards, or other web-based solutions. This project serves as a practical reference that will allow me to easily recall and apply what I have learned.''' 
def stream_data():
    for word in description.split(" "):
        yield word + " "
        time.sleep(0.02)
st.write_stream(stream_data)
st.divider()


st.markdown("<h3 '>Data viewer</h3>", unsafe_allow_html=True)


