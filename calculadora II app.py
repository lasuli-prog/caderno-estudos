import streamlit as st

st.header("Calculadora de Juros Compostos")

capital = st.number_input("Capital")
taxa = st.number_input("Taxa (%)")
tempo = st.number_input("Tempo")

montante = capital * (1 + taxa/100) ** tempo

if st.button("Calcular montante"):
  st.write("Montante:", montante) 
