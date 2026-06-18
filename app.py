import streamlit as st

st.title("Zyro Dynamics HR Help Desk")

question = st.text_input("Ask an HR Question")

if question:
    response = ask_bot(question)
    st.write("HR Bot Response")
    st.write(response["answer"])
