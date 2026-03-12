import streamlit as st

st.title("Caderno")

materia = st.text_input("Matemática")

anotacao = st.text_area("Anotação da aula")

if st.button("Salvar"):
  st.sucess("Anotação salva!")
