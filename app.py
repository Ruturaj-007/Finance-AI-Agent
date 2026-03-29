import streamlit as st
from data import get_stock_price, extract_price, get_company_profile, extract_profile, build_final_data, prepare_for_ai
from agent import analyze

st.title("Simple stock checker")

ticker = st.text_input("Enter ticker")
if st.button("Get Price"):
    final = build_final_data(ticker)

    price = final["price_data"]
    profile = final["profile_data"]
    ai_input = prepare_for_ai(final)

    st.markdown("---")
    st.subheader("AI Input (Cleaned)")
    st.json(ai_input)

    st.subheader(final["company"])

    col1, col2, col3 = st.columns(3)

    col1.metric("💰 Price", price["price"])
    col2.metric("📉 Change", price["change"])
    col3.metric("📊 Volume", price["volume"])

    st.markdown("---")
    st.subheader("Company Info")

    st.write(f"**Sector:** {profile['sector']}")
    st.write(f"**Industry:** {profile['industry']}")
    st.write(f"**Country:** {profile['country']}")
    st.write(f"**Employees:** {profile['employees']}")
    st.write(f"**Website:** {profile['website']}")

    report = analyze(ai_input)

    st.markdown("---")
    st.subheader("AI Analysis")
    st.write(report)