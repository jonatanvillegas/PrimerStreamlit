import streamlit as st
import pandas as pd
import plotly.express as px

st.subheader("Filtrar Datos y Captura de Datos")
st.write("El procesamiento de datos a través de Ciencia de Datos usando Streamlit de Python")

dfDatos = pd.read_csv('http://raw.githubusercontent.com/gcastano/datasets/main/gapminder_data.csv')

# Mostrar la tabla de los registros
# st.metric("***Registros Totales***", len(dfDatos))
# st.dataframe(dfDatos, use_container_width=True)

# crear filtros 
continent_filter = st.multiselect(
    "Selecciona los continentes:",
    options=dfDatos['continent'].unique(),
    default=dfDatos['continent'].unique()
)

# Campo de entrada para el pais
country_filter = st.text_input(
    "Escriba el nombre del País (opcional):",
    value= ""
)

# Rango de edad
age_range = st.slider( 
    "Selecciona el Rango de Edad:", 
    min_value=int(dfDatos['median_age_year'].min()), 
    max_value=int(dfDatos['median_age_year'].max()), 
    value=(int(dfDatos['median_age_year'].min()), int(dfDatos['median_age_year'].max()))
)

# Filtrar los datos basados en las selecciones
# filtered_data = dfDatos[
#     (dfDatos['continent'].isin(continent_filter)) &
#     (dfDatos['country'].str.contains(country_filter, case=False, na=False)) &
#     (dfDatos['median_age_year'] >= age_range[0]) &
#     (dfDatos['median_age_year'] <= age_range[1])
# ]

filtered_data = dfDatos.copy()

if continent_filter:
    filtered_data = filtered_data[filtered_data['continent'].isin(continent_filter)]
if country_filter:
    filtered_data = filtered_data[filtered_data['country'].str.contains(country_filter, case=False, na=False)]

filtered_data = filtered_data[
    (filtered_data['median_age_year'] >= age_range[0]) &
    (filtered_data['median_age_year'] <= age_range[1])
]

st.metric("***Registros Totales Filtrados***", len(filtered_data)) 
st.dataframe(filtered_data, use_container_width=True)
