# Proyecto de Navegación con Streamlit

Este proyecto es una aplicación web desarrollada en Streamlit que incluye múltiples vistas y funcionalidades organizadas en una barra de navegación. Las vistas incluyen una página de inicio, una sección "Acerca de" y dos proyectos: un sistema de ventas y un chatbot interactivo.

## Funcionalidades

- **Inicio**: Página principal de la aplicación.
- **Acerca de**: Información sobre el proyecto o los autores.
- **Ventas**: Sistema de ventas, posiblemente para visualizar o gestionar productos.
- **Chat Bot**: Un chatbot interactivo para comunicación o asistencia automatizada.

## Estructura del Proyecto

La aplicación está organizada con diferentes vistas dentro de la carpeta `vistas`, que contiene los siguientes archivos:

- `home.py`: Vista de la página principal.
- `acerca_de.py`: Vista de la sección "Acerca de".
- `ventas.py`: Vista para el sistema de ventas.
- `chatbot.py`: Vista para el chatbot.

## Requisitos

- Python 3.8 o superior
- [Streamlit](https://streamlit.io/) - Framework de desarrollo web para aplicaciones de Python.

## Instalación

1. Clona este repositorio:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
    ```

2. Crea un entorno virtual y actívalo:
    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    ```

3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

4. Asegúrate de que `Streamlit` esté instalado:
    ```bash
    pip install streamlit
    ```

## Ejecución de la Aplicación

Para ejecutar la aplicación, utiliza el siguiente comando en la terminal dentro del directorio del proyecto:

```bash
streamlit run appwebST.py
