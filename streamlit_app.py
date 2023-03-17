# Procesamiento de datos
import pandas as pd
import numpy as np

# Imágenes
import json
import requests

# Gráficos
import altair as alt
import plotly.figure_factory as ff
import plotly.express as px

# Integración
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu

# Configuración de página

st.set_page_config(
    page_title="Detección de objetos para conducción autónoma",
    page_icon=":car",
    )

st.title("Detección de objetos para conducción autónoma")

selected = option_menu(
    menu_title=None,
    options=["Inicio","Datos","Modelo", "Resultados"],
    icons=["house", "clipboard-data", "boxes", "card-checklist"],
    default_index=0,
    orientation="horizontal",
)

# Sección 1

if selected == "Inicio":
 
    st_lottie(requests.get("https://assets9.lottiefiles.com/packages/lf20_ndLURGQdmU.json").json(), height=450, key="car")

    st.markdown("## Introducción")

    st.markdown('<div style="text-align: justify;">Saber dónde están los demás vehículos en la carretera y ser capaz de anticipar hacia dónde se dirigen a continuación es esencial en un coche autoconducido. También hay que saber a qué distancia están, en qué dirección van y a qué velocidad se mueven. Lo mismo que hacemos con nuestros propios ojos cuando conducimos. La detección y el seguimiento de objetos es un concepto fundamental en la visión por ordenador avanzada.</div>', unsafe_allow_html=True)
    
    st.write("")

    st.write("")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### Problema")

        st.markdown('<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</div>', unsafe_allow_html=True)
    
    with col2:

        st.write("")

        data_path = "/Users/marta/Documents/GitHub/Object-detection-for-self-driving-cars"

        img = f"{data_path}/img_data/1478019952686311006_jpg.rf.54e2d12dbabc46be3c78995b6eaf3fee.jpg"

        st.image(img, caption = "Imagen")

    col3, col4 = st.columns(2)

    with col3:

        st.write("")

        data_path = "/Users/marta/Documents/GitHub/Object-detection-for-self-driving-cars"

        img = f"{data_path}/img_data/1478019952686311006_jpg.rf.54e2d12dbabc46be3c78995b6eaf3fee.jpg"

        st.image(img, caption = "Imagen")

    with col4:

        st.markdown("### Objetivo")

        st.markdown('<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</div>', unsafe_allow_html=True)
    
    st.markdown("### Conclusión")

    st.markdown('<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</div>', unsafe_allow_html=True)
    

# Sección 2
       
if selected == "Datos":
 
    st_lottie(requests.get("https://assets5.lottiefiles.com/packages/lf20_uxsajfrq.json").json(), height=450, key="charts")

    st.markdown("## Análisis del conjunto de datos")

    st.markdown('<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)

    df_data = pd.read_csv("/Users/marta/Documents/GitHub/Object-detection-for-self-driving-cars/data_info.csv")

    with col1:

        fig = px.sunburst(df_data, path=["set","class"], values="image")

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        st.markdown("### División del conjunto de datos train/val/test")

        st.markdown('<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</div>', unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)

    with col3:

        st.markdown("### Distribución de las clases")

        st.markdown('<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</div>', unsafe_allow_html=True)
    
    with col4:

        fig = px.bar(df_data, x="image", y="set", color="class")

        st.plotly_chart(fig, use_container_width=True)


if selected == "Modelo":
 
    st_lottie(requests.get("https://assets3.lottiefiles.com/private_files/lf30_wo802rvq.json").json(), height=450, key="model")

    st.markdown("## Detección de objetos con YOLOv8")

    st.markdown('<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])

    with col1:

        st.markdown("### Ociones de visualización")

        st.multiselect("Escoge lo que quieres ver", ["peaton", "coche", "semaforo"])

        st.slider("Escoge una imagen", max_value=100, value=50)

        st.slider("Confianza", max_value=1.0, value=0.5, step=0.1)

        st.slider("Superposición", max_value=1.0, value=0.3, step=0.1)

    with col2:

        st.write("")

        data_path = "/Users/marta/Documents/GitHub/Object-detection-for-self-driving-cars"

        img = f"{data_path}/img_data/1478019952686311006_jpg.rf.54e2d12dbabc46be3c78995b6eaf3fee.jpg"

        st.image(img, caption = "Resultados")

    st.markdown("## Observaciones")

    st.markdown('<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</div>', unsafe_allow_html=True)
    
if selected == "Resultados":

    st_lottie(requests.get("https://assets2.lottiefiles.com/packages/lf20_noohi61b.json").json(), height=500, key="results")

    st.markdown("## Resultados")

    st.markdown('<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</div>', unsafe_allow_html=True)
    
    # Add histogram data
    x1 = np.random.randn(200) - 2
    x2 = np.random.randn(200)
    x3 = np.random.randn(200) + 2

    # Group data together
    hist_data = [x1, x2, x3]

    group_labels = ['Group 1', 'Group 2', 'Group 3']

    # Create distplot with custom bin_size
    fig = ff.create_distplot(
            hist_data, group_labels, bin_size=[.1, .25, .5])

    # Plot!
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Define a custom colorscale")
    df = px.data.iris()
    fig = px.scatter(
        df,
        x="sepal_width",
        y="sepal_length",
        color="sepal_length",
        color_continuous_scale="reds",
    )

    tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
    with tab1:
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)
    with tab2:
        st.plotly_chart(fig, theme=None, use_container_width=True)


# streamlit run /Users/marta/Documents/GitHub/Object-detection-for-self-driving-cars/streamlit_app.py