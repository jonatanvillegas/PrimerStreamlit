import streamlit as st


st.set_page_config(page_title="Home", layout="wide")

# Estilos personalizados
st.markdown("""
    <style>
    .header {
        font-size: 40px;
        color: #2C3E50;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    .subheader {
        font-size: 22px;
        color: #3498DB;
        text-align: center;
        margin-bottom: 10px;
    }
    .section {
        margin-top: 50px;
    }
    .card {
        background-color: #f7f7f7;
        border-radius: 10px;
        padding: 20px;
        margin: 10px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .testimonial {
        font-style: italic;
        color: #34495E;
        margin: 15px 0;
    }
    .footer {
        text-align: center;
        font-size: 14px;
        color: #7F8C8D;
        margin-top: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

# Encabezado
st.markdown('<div class="header">Bienvenidos a Nuestra Página Informativa</div>', unsafe_allow_html=True)
st.markdown('<div class="subheader">Conoce nuestros servicios y el equipo que nos respalda</div>', unsafe_allow_html=True)

# Sección: Acerca de nosotros
st.markdown('<div class="section">', unsafe_allow_html=True)
st.markdown("## Acerca de Nosotros")
st.write("Somos una empresa comprometida con la excelencia y la satisfacción de nuestros clientes. Nos dedicamos a ofrecer servicios de alta calidad en [área de especialización]. Nuestro equipo está compuesto por profesionales apasionados que trabajan para crear soluciones innovadoras.")

# Sección: Nuestros Servicios
st.markdown("## Nuestros Servicios")
st.write("Explora nuestros servicios y descubre cómo podemos ayudarte a alcanzar tus objetivos.")
cols = st.columns(3)

# Card 1
with cols[0]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image("https://via.placeholder.com/150", width=150)
    st.write("**Servicio 1**")
    st.write("Descripción breve del servicio 1.")
    st.markdown('</div>', unsafe_allow_html=True)

# Card 2
with cols[1]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image("https://via.placeholder.com/150", width=150)
    st.write("**Servicio 2**")
    st.write("Descripción breve del servicio 2.")
    st.markdown('</div>', unsafe_allow_html=True)

# Card 3
with cols[2]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image("https://via.placeholder.com/150", width=150)
    st.write("**Servicio 3**")
    st.write("Descripción breve del servicio 3.")
    st.markdown('</div>', unsafe_allow_html=True)

# Sección: Testimonios
st.markdown("## Testimonios")
st.write("Lo que nuestros clientes dicen de nosotros:")
with st.container():
    st.markdown('<div class="testimonial">"Excelente servicio, muy profesionales y siempre atentos a nuestras necesidades."</div>', unsafe_allow_html=True)
    st.write("– Cliente A")
    st.markdown('<div class="testimonial">"Recomiendo totalmente a esta empresa. Sus soluciones fueron innovadoras y eficaces."</div>', unsafe_allow_html=True)
    st.write("– Cliente B")
    st.markdown('<div class="testimonial">"El equipo es increíble, siempre dispuesto a ayudar y solucionar problemas rápidamente."</div>', unsafe_allow_html=True)
    st.write("– Cliente C")

# Sección: Nuestro Equipo
st.markdown("## Nuestro Equipo")
st.write("Conoce a las personas detrás de nuestros éxitos.")
team_cols = st.columns(3)

# Card de miembro del equipo 1
with team_cols[0]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image("https://via.placeholder.com/100", width=100)
    st.write("**Nombre del Miembro 1**")
    st.write("Cargo: CEO")
    st.write("Experto en [campo de especialización].")
    st.markdown('</div>', unsafe_allow_html=True)

# Card de miembro del equipo 2
with team_cols[1]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image("https://via.placeholder.com/100", width=100)
    st.write("**Nombre del Miembro 2**")
    st.write("Cargo: CTO")
    st.write("Especialista en tecnología y desarrollo de proyectos.")
    st.markdown('</div>', unsafe_allow_html=True)

# Card de miembro del equipo 3
with team_cols[2]:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.image("https://via.placeholder.com/100", width=100)
    st.write("**Nombre del Miembro 3**")
    st.write("Cargo: Gerente de Marketing")
    st.write("Creativo y apasionado por la comunicación y el marketing digital.")
    st.markdown('</div>', unsafe_allow_html=True)

# Sección: Contáctanos
st.markdown("## Contáctanos")
st.write("¡Nos encantaría escuchar de ti! Llena el siguiente formulario y nos pondremos en contacto contigo.")

with st.form("contact_form"):
    st.text_input("Nombre")
    st.text_input("Correo Electrónico")
    st.text_area("Mensaje")
    submitted = st.form_submit_button("Enviar")
    if submitted:
        st.success("Gracias por contactarnos. ¡Te responderemos pronto!")

# Pie de página
st.markdown('<div class="footer">© 2023 Nuestra Empresa. Todos los derechos reservados.</div>', unsafe_allow_html=True)
