import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Vehículos US", layout="wide")

# Encabezado (requisito)
st.header("Panel interactivo: Anuncios de venta de coches en Estados Unidos")

# Cargar datos (asegúrate que el CSV está en la raíz del proyecto)
DATA_PATH = "vehicles_us.csv"

@st.cache_data
def load_data(path):
    return pd.read_csv(path)

car_data = load_data(DATA_PATH)

st.write("Vista rápida de los datos:")
st.dataframe(car_data.head())

st.divider()
st.subheader("Visualizaciones interactivas")

# Botón 1: Histograma (requisito)
hist_button = st.button("Construir histograma")
if hist_button:
    st.write("Histograma del odómetro")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botón 2: Dispersión (requisito)
scatter_button = st.button("Construir diagrama de dispersión")
if scatter_button:
    st.write("Diagrama de dispersión: precio vs odómetro")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
