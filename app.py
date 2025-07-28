import streamlit as st

# Basic UI test
st.set_page_config(page_title="Mental Health Analyzer")

st.title("🧠 Mental Health Analyzer")
st.write("Welcome to your first deployed Streamlit app, Brian!")

if st.button("Test Me"):
    st.success("Streamlit is working fine!")

