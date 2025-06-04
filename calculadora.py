import streamlit as st

# Esta línea debe ser la primera instrucción de Streamlit
st.set_page_config(page_title="Calculadora", layout="centered")

# Fondo rosa suave
page_bg = """
<style>
body {
    background-color: #fffff;
}
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

st.title("📱 Calculadora tipo móvil")

# Estado inicial
if "expresion" not in st.session_state:
    st.session_state.expresion = ""

# Funciones
def pulsar(valor):
    st.session_state.expresion += str(valor)

def borrar():
    st.session_state.expresion = ""

def calcular():
    try:
        resultado = eval(st.session_state.expresion)
        st.session_state.expresion = str(resultado)
    except:
        st.session_state.expresion = "❌ Error"

# Pantalla de entrada (desactivada para que no se edite a mano)
st.text_input("Pantalla", value=st.session_state.expresion, disabled=True)

# Botones tipo calculadora
botones = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

# Dibujar botones
for fila in botones:
    cols = st.columns([1, 1, 1, 1])
    for i, val in enumerate(fila):
        if val == "=":
            cols[i].button("=", use_container_width=True, on_click=calcular)
        elif val in ["/", "*", "-", "+"]:
            # Traducimos símbolo para que se vea bonito
            if val == "/":
                texto = "÷"
            elif val == "*":
                texto = "×"
            elif val == "-":
                texto = "−"
            elif val == "+":
                texto = "+"
            cols[i].button(texto, use_container_width=True, on_click=pulsar, args=(val,))
        else:
            cols[i].button(val, use_container_width=True, on_click=pulsar, args=(val,))

# Botón de borrar abajo
st.button("🧹 Borrar todo", on_click=borrar)