import streamlit as st

st.header("Calculadora de Juros Simples")

capital = st.number_input("Capital inicial")
taxa = st.number_input("Taxa (%)")
tempo = st.number_input("Tempo")

juros = capital * (taxa/100) * tempo

if st.button("Calcular"):
  st.write("Juros:", juros)
