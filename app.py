import streamlit as st
from data import get_stock_price, extract_price

st.title("Simple stock checker")

ticker = st.text_input("Enter ticker")

if st.button("Get price"):
    raw = get_stock_price(ticker)
    clean = extract_price(raw)
    
    st.write("Clean data")
    st.json(clean)
    st.success("Stock details fetched successfully")