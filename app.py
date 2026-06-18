import streamlit as st

st.title("Zyro Dynamics HR Help Desk")

question = st.text_input("Ask an HR Question")

if question:
    st.subheader("HR Bot Response")
    st.write("Demo chatbot deployed successfully.")
