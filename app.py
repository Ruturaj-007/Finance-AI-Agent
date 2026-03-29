import streamlit as st
from data import get_stock_price

st.title("Simple stock checker")

ticker = st.text_input("Enter ticker")

if st.button("Get price"):
    data = get_stock_price(ticker)
    st.write(data)
    st.success("Stock details fetched successfully")