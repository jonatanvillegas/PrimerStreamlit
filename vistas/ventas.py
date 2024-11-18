import streamlit as st 
import pandas as pd 
import plotly.express as px

import datetime



st.header("Filtrado y captura de datos")
st.write("El procesamiento de datos a travez de la ciencia de datos usuando Streamlit de python")

#crear tres columnas y filtrar por pais, minimo de hijos y espectativa de vida.

c1, c2, c3= st.columns((3))

with c1:
    par_Pais = st.text_input("Pais:", placeholder="Escriba el nombre del pais")

with c2: 
    par_Fertilidad = st.number_input("Minimo numero de hijos",  min_value=0, max_value=100, step= 1)
    
with c3:
    par_RangoExpectatiDeVida= st.slider("Rango de expectativa de vida", min_value=10, max_value=100, value=(10,100))


dfDatos = pd.read_csv("https://raw.githubusercontent.com/gcastano/datasets/main/gapminder_data.csv")

if par_Pais !="":
    dfDatos= dfDatos[dfDatos["country"].str.upper().str.contains(par_Pais.upper())]

if par_Fertilidad >0:
    dfDatos= dfDatos[dfDatos["fertility"]>=par_Fertilidad]
    
dfDatos =dfDatos [(dfDatos["lifeExpectancy"]>=par_RangoExpectatiDeVida[0]) & (dfDatos["lifeExpectancy"]<=par_RangoExpectatiDeVida)]

st.metric("Registros Totales", len (dfDatos))
st.dataframe(dfDatos, use_container_width=True)

