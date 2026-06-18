import streamlit as st

st.title("Zyro Dynamics HR Help Desk")

question = st.text_input("Ask an HR Question")

if question:
    st.write("HR Bot Response")
