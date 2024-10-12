import streamlit as st
from PIL import Image

st.set_page_config(layout="wide", page_title="Mapping Demo", page_icon="🌍")


# Título y subtítulo
st.title("Actividades: [Nuevas Tecnologías]")
st.subheader("Aquí encontraras las actividades que he realizado en este 3er nivel de esta asignatura")

# Imagen de fondo
image = Image.open("./static/fondopy.jpg") 
st.image(image, width=500, use_column_width=True)  

# Integrantes
st.header("Practicante en Desarrollo de Software")

col1 = st.columns(1)[0]


with col1:
    st.image("./static/Multimedia.jfif", width=200)  # Reemplaza con la ruta de la foto
    st.write("**<Jorge Eduardo Muñoz Quintero/>**")
    st.write("<Desarrollador/>")


# Descripción del proyecto
st.header("Trabajos")
st.write("""
La función principal es reunir todas las evidencias de los trabajos que se van realizando en la asignatura de nuevas tecnologías para la programación ya que es mas ordenado de esta manera y se puede practicar con este tipo de trabajos""")


# Puedes añadir secciones como:
# - Tecnología utilizada
# - Resultados esperados
# - Presentación de resultados (fecha y formato)
# - Contacto para preguntas
st.header("Tecnologías usadas")
st.write("""
[Python, Pandas, Firebase y Streamlit]
""")

# Footer con links
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px;">
        <a href="https://www.google.com">Google</a> |
        <a href="https://www.facebook.com">Facebook</a> |
        <a href="https://www.linkedin.com">LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True,
)