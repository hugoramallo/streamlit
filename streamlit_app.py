import streamlit as st

st.set_page_config(page_title="Demo App", page_icon="📊", layout="centered")

st.title("📊 Demo de Streamlit")
st.write("¡Bienvenido a tu primera app con Streamlit en GitHub!")

# Widgets interactivos
nombre = st.text_input("¿Cómo te llamas?", "")
edad = st.slider("¿Qué edad tienes?", 0, 100, 25)

if nombre:
    st.success(f"Hola, {nombre}. Tienes {edad} años.")

# Gráfico simple
import pandas as pd
import numpy as np

data = pd.DataFrame({
    'x': np.arange(1, 11),
    'y': np.random.randint(1, 100, 10)
})

st.line_chart(data.set_index('x'))
