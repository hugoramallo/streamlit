import streamlit as st
import sqlite3
import pandas as pd

def get_connection():
    return sqlite3.connect("empresa.db")

def get_roles():
    conn = get_connection()
    roles = conn.execute("SELECT id, nombre FROM roles").fetchall()
    conn.close()
    return roles

st.title("Gestión de Usuarios con Roles")

menu = st.sidebar.selectbox("Opciones", ["Ver usuarios", "Agregar", "Actualizar", "Eliminar"])

# Opción 1 - Ver usuarios (con nombre del rol)
if menu == "Ver usuarios":
    conn = None
    try:
        conn = get_connection()
        df = pd.read_sql_query("""
            SELECT usuarios.id, usuarios.nombre, usuarios.email, roles.nombre as rol
            FROM usuarios
            LEFT JOIN roles ON usuarios.rol_id = roles.id
        """, conn)
        st.dataframe(df)
    except Exception as e:
        st.error(f"Error al consultar la base de datos: {e}")
    finally:
        if conn:
            conn.close()

# Opción 2: Agregar nuevo usuario con rol
elif menu == "Agregar":
    nombre = st.text_input("Nombre")
    email = st.text_input("Email")
    roles = get_roles()
    rol_dict = {nombre: id for id, nombre in roles}
    rol_nombre = st.selectbox("Rol", list(rol_dict.keys()))

    if st.button("Agregar"):
        if nombre and email and rol_nombre:
            conn = None
            try:
                conn = get_connection()
                rol_id = rol_dict[rol_nombre]
                conn.execute(
                    "INSERT INTO usuarios (nombre, email, rol_id) VALUES (?, ?, ?)",
                    (nombre, email, rol_id)
                )
                conn.commit()
                st.success("Usuario agregado")
            except Exception as e:
                st.error(f"No se pudo agregar el usuario: {e}")
            finally:
                if conn:
                    conn.close()
        else:
            st.warning("Por favor, completa todos los campos.")

# Opción 3: Actualizar nombre y rol
elif menu == "Actualizar":
    id_usuario = st.number_input("ID del usuario", min_value=1)
    nuevo_nombre = st.text_input("Nuevo nombre")
    roles = get_roles()
    rol_dict = {nombre: id for id, nombre in roles}
    nuevo_rol = st.selectbox("Nuevo rol", list(rol_dict.keys()))

    if st.button("Actualizar"):
        conn = None
        if nuevo_nombre:
            try:
                conn = get_connection()
                result = conn.execute(
                    "UPDATE usuarios SET nombre = ?, rol_id = ? WHERE id = ?",
                    (nuevo_nombre, rol_dict[nuevo_rol], id_usuario)
                )
                conn.commit()
                if result.rowcount == 0:
                    st.warning("No se encontró un usuario con ese ID.")
                else:
                    st.success("Usuario actualizado")
            except Exception as e:
                st.error(f"No se pudo actualizar el usuario: {e}")
            finally:
                if conn:
                    conn.close()
        else:
            st.warning("El nombre no puede estar vacío.")

# Opción 4: Eliminar usuario
elif menu == "Eliminar":
    id_borrar = st.number_input("ID del usuario a eliminar", min_value=1)

    if st.button("Eliminar"):
        conn = None
        try:
            conn = get_connection()
            result = conn.execute("DELETE FROM usuarios WHERE id = ?", (id_borrar,))
            conn.commit()
            if result.rowcount == 0:
                st.warning("No se encontró un usuario con ese ID.")
            else:
                st.warning("Usuario eliminado")
        except Exception as e:
            st.error(f"No se pudo eliminar el usuario: {e}")
        finally:
            if conn:
                conn.close()