import streamlit as st
from data import get_stock_price, extract_price, get_company_profile, extract_profile

st.title("Simple stock checker")

ticker = st.text_input("Enter ticker")
if st.button("Get Price"):
    raw = get_stock_price(ticker)
    clean = extract_price(raw)

    profile_raw = get_company_profile(ticker)
    profile = extract_profile(profile_raw)
    st.markdown("---")
    st.subheader("Company Info")

    st.write(f"**Sector:** {profile['sector']}")
    st.write(f"**Industry:** {profile['industry']}")
    st.write(f"**Country:** {profile['country']}")
    st.write(f"**Employees:** {profile['employees']}")
    st.write(f"**Website:** {profile['website']}")

    if "error" in clean:
        st.error(clean["error"])
    else:
        st.subheader(clean["company"])

        col1, col2, col3 = st.columns(3)

        col1.metric("💰 Price", clean["price"])
        col2.metric("📉 Change", clean["change"])
        col3.metric("📊 Volume", clean["volume"])