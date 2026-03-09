import streamlit as st
import pandas as pd
import sqlite3

conn = sqlite3.connect("books.db")

df = pd.read_sql_query("SELECT * FROM books", conn)

st.title("Web Scraping Data Dashboard")

st.write("Dataset Preview")
st.dataframe(df)

st.write("Price Distribution")
st.bar_chart(df["Price"])

st.write("Statistics")
st.write(df.describe())

st.subheader("Average Book Price")
st.write(df["price"].mean())

st.subheader("Rating Distribution")
st.bar_chart(df["rating"].value_counts())

st.subheader("Top 10 Most Expensive Books")
st.dataframe(df.sort_values("price", ascending=False).head(10))