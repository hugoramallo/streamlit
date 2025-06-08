import streamlit as st
import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

# Ejercicios de introducción a Streamlit

#"""1. Hola mundo interactivo:
 #  - Crea una app que permita al usuario escribir su nombre y muestra un saludo dinámico."""
#st.title("Hola Mundo!")
#nombre = st.text_input("¿Cómo te llamas?")
#st.success(f"Hola {nombre}")

#"""2. Contador de clics:
 #  - Crea un botón que incremente un contador cada vez que se pulsa, usando st.session_state."""
#if 'contador' not in st.session_state:
  #  st.session_state.contador = 0

#if st.button("Hac click aquí."):
 #   st.session_state.contador += 1

#st.write(f"Has hecho click {st.session_state.contador} veces")

#"""3. Selector de color:
#   - Permite al usuario seleccionar un color con st.color_picker() y muestra el valor hexadecimal."""
#color = st.color_picker("Elige el color que quieras","#00f900")
#st.write(f"Has seleccionado el color {color}")
#"""4. DataFrame y visualización:
 #  - Crea un DataFrame con nombres y edades, muéstralo con st.dataframe() y dibuja un gráfico de barras."""

#"""5. Encuesta:
#   - Crea un sistema de votación con st.radio() o st.selectbox() y muestra los resultados en una gráfica."""
# data = pd.DataFrame({"Nombre": ["Ana", "Luis", "Carlos","Pablo"], "Edad": [25, 30, 22, 40]})
#st.dataframe(data)
#st.bar_chart(data.set_index("Nombre"))

#"""6. Juego "Adivina el número":
#   - El sistema genera un número aleatorio. El usuario intenta adivinarlo y recibe feedback."""
import random
if 'secreto' not in st.session_state:
    st.session_state.secreto = random.randint(1,100)
guess = st.number_input("Adivina el número (1-100)", min_value=1, max_value=100, step=1)

# Botón para comprobar el número
if st.button("Comprobar"):
    if guess == st.session_state.secreto:
        st.success("¡Correcto!")
        st.session_state.secreto = random.randint(1, 100)  # Genera nuevo número secreto
    elif guess < st.session_state.secreto:
        st.warning("Demasiado bajo")
    else:
        st.warning("Demasiado alto")


"""7. Conversor de temperatura:
   - Permite convertir entre Celsius y Fahrenheit."""
# Selector de modo de conversión
modo = st.radio("Convertir:", ["Celsius a Fahrenheit", "Fahrenheit a Celsius"])

# Entrada de temperatura
temp = st.number_input("Temperatura")

# Realiza la conversión y muestra el resultado
if modo == "Celsius a Fahrenheit":
    st.write(f"{temp}°C = {(temp * 9/5) + 32}°F")
else:
    st.write(f"{temp}°F = {(temp - 32) * 5/9:.2f}°C")

"""8. Subida de imagen:
   - Permite al usuario subir una imagen y muestra su nombre, tamaño y previsualización."""

# 9. Subida de imagen
# Carga una imagen desde el equipo
archivo = st.file_uploader("Sube una imagen", type=["png", "jpg", "jpeg"])

"""9. Calculadora básica:
   - Usa st.number_input() para ingresar dos números y botones para realizar suma, resta, multiplicación y división."""
