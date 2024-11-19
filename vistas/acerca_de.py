import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Acerca de", page_icon="📖")

# Contenido de la vista "Acerca de"
st.title("Acerca de")
st.write(
    """
    Bienvenido a la sección **Acerca de** de nuestra aplicación. Aquí encontrarás información sobre el propósito,
    los objetivos y las personas detrás de este proyecto.
    """
)

# Sección: Propósito del proyecto
st.header("Propósito del Proyecto")
st.write(
    """
    Este proyecto tiene como objetivo proporcionar una plataforma intuitiva y eficiente para realizar
    análisis de datos de manera interactiva utilizando **Streamlit**. Busca simplificar el acceso a la 
    información y ofrecer herramientas útiles para la toma de decisiones.
    """
)

# Sección: Características
st.header("Características Principales")
st.markdown(
    """
    - 🎯 **Filtros interactivos** para personalizar la información mostrada.
    - 📊 Visualización clara y accesible de datos.
    - 🌐 Acceso a datos globales de diversas fuentes.
    """
)

# Sección: Sobre los creadores
st.header("Sobre los Creadores")
st.write(
    """
    Este proyecto fue desarrollado por un equipo apasionado por la tecnología y la ciencia de datos. 
    Si deseas saber más o colaborar con nosotros, no dudes en ponerte en contacto.
    """
)

# Información de contacto
st.subheader("Contacto")
st.write(
    """
    - 📧 Correo electrónico: [contacto@example.com](mailto:contacto@example.com)
    - 🌐 Sitio web: [www.ejemplo.com](https://www.ejemplo.com)
    - 🐦 Twitter: [@Ejemplo](https://twitter.com/Ejemplo)
    """
)

# Imagen o logo (opcional)
st.image("https://via.placeholder.com/300x100?text=Logo", caption="Nuestro Logo", use_column_width=True)
