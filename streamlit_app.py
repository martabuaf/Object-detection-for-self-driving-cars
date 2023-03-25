# Procesamiento de datos
import pandas as pd
import numpy as np

# Imágenes
import json
import requests

# Gráficos
import plotly.express as px

# Integración
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_option_menu import option_menu
from streamlit_extras.dataframe_explorer import dataframe_explorer
from streamlit_extras.add_vertical_space import add_vertical_space

# Parámetros iniciales

cmap = {"dark_green": 'rgb(0,112,88)', "green": 'rgb(80,145,125)', "blue_green": 'rgb(38,160,146)', "yellow": 'rgb(239,199,73)', "orange": 'rgb(229,93,47)'}

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


# Pag 1 - Inicio

if selected == "Inicio":
 
    st_lottie(requests.get("https://assets9.lottiefiles.com/packages/lf20_ndLURGQdmU.json").json(), height=450, key="car")

    st.markdown("## Introducción")

    st.markdown('<div style="text-align: justify;"><p>La conducción autónoma es una tecnología innovadora y prometedora que ha capturado la atención de la industria automovilística y de los consumidores en todo el mundo. Esta tecnología utiliza sistemas avanzados de inteligencia artificial y robótica para permitir que los vehículos operen de forma independiente, sin necesidad de intervención humana. Sin embargo, a pesar de sus promesas, la conducción autónoma todavía enfrenta importantes desafíos y limitaciones que deben abordarse antes de que se pueda alcanzar todo su potencial.</p></div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("### Problema")

        st.markdown('<div style="text-align: justify;">Uno de los principales desafíos de la conducción autónoma es la complejidad de los entornos de conducción. Los vehículos autónomos deben ser capaces de percibir y comprender su entorno, tomar decisiones de conducción en tiempo real y controlar sus interacciones con otros usuarios de la carretera, como los peatones, ciclistas y conductores de otros vehículos.</p><p>Es necesario que los vehículos autónomos consigan detectar y responder a estas interacciones de forma segura y eficiente, para evitar accidentes y conflictos.</p></div>', unsafe_allow_html=True)
    
    with col2:

        add_vertical_space(5)

        img = "foto_predict/foto.jpg"

        st.image(img, caption = "Imagen original")

    col3, col4 = st.columns(2)

    with col3:

        add_vertical_space(5)

        img = "foto_predict/foto_results.jpg"

        st.image(img, caption = "Resultados de la detección de objetos")

    with col4:

        st.markdown("### Objetivo")

        st.markdown('<div style="text-align: justify;"><p>A través de la detección de objetos se consigue proporcionar información precisa y en tiempo real sobre el entorno del vehículo. Al eliminar la posibilidad de errores humanos, se reducirán significativamente el número de accidentes de tráfico y, además, la conducción autónoma puede optimizar la velocidad y la ruta de conducción, lo que puede reducir el tiempo de viaje, disminuir la congestión del tráfico y ahorrar combustible.</p><p> Por último, la conducción autónoma puede proporcionar una mayor comodidad y accesibilidad para personas con discapacidad o movilidad reducida.</div>', unsafe_allow_html=True)
    
    st.markdown("### Conclusión")

    st.markdown('<div style="text-align: justify;"><p>La conducción autónoma es una tecnología con un gran potencial para mejorar la seguridad, la eficiencia y la comodidad del transporte. Sin embargo, todavía hay desafíos importantes que deben abordarse antes de que se pueda alcanzar plenamente su potencial.</p><p>La complejidad de los entornos de conducción, la interacción con otros usuarios de la carretera y la regulación gubernamental son solo algunos de los desafíos que enfrenta la conducción autónoma. Con el tiempo y los avances tecnológicos y regulatorios, es probable que la conducción autónoma desempeñe un papel cada vez más importante en el futuro del transporte.</p></div>', unsafe_allow_html=True)
    

# Pag 2 - Datos
       
if selected == "Datos":

    st_lottie(requests.get("https://assets5.lottiefiles.com/packages/lf20_uxsajfrq.json").json(), height=450, key="charts")

    st.markdown("## Análisis del conjunto de datos")

    st.markdown('<div style="text-align: justify;"><p>El conjunto de datos que hemos utilizado para entrenar la red neuronal lo encontramos en <a href="https://www.kaggle.com/datasets/sshikamaru/udacity-self-driving-car-dataset" target = "_blank"> Kaggle</a> e incluye imágenes de conducción e información sobre los elementos ya etiquetados en las imágenes.</p>Llevamos a cabo el análisis de los datos para extraer información útil y relevante y poder encontrar patrones, tendencias y relaciones que puedan ayudar a la inteligencia artificial a tomar decisiones precisas y en tiempo real mientras conduce.</p></div>', unsafe_allow_html=True)
    
    add_vertical_space(1)

    col1, col2 = st.columns([6,5])

    df_class = pd.read_csv("class_info.csv")

    with col1:

        fig = px.sunburst(df_class, path=["set","class"], values="count", color="set", color_discrete_map = {'train': cmap["dark_green"], 'validation' : cmap["blue_green"], 'test': cmap["orange"]})

        fig.update_traces(textinfo="label+percent parent")

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        st.markdown("### División del conjunto de datos")

        st.markdown('<div style="text-align: justify;"><p>Para que el entrenamiento del modelo se realize de forma óptima llevamos a cabo la división del conjunto de datos, para lo que definimos tres subconjuntos: el conjunto de entrenamiento (train), validación (val) y prueba (test).</p><p>Al separar el conjunto de datos nos aseguramos de que el modelo pueda aprender de manera efectiva y generalizar bien en diferentes entornos, evitando el sobreajuste.</p></div>', unsafe_allow_html=True)
    
    add_vertical_space(1)

    col3, col4 = st.columns([5,6])

    with col3:

        st.markdown("### Distribución de las clases")

        st.markdown('<div style="text-align: justify;"><p>En un modelo de clasificación es importante que las clases se encuentren equilibradas. Si una clase tiene significativamente más ejemplos que la otra, el modelo estará sesgado hacia esa clase y tendrá dificultades para clasificar las clases menos representadas, suponiendo una disminución de la precisión general del modelo.</p><p>Por lo tanto, es importante que las clases se encuentren bien distribuidas para garantizar que el modelo tenga una precisión y un rendimiento óptimos.</p></div>', unsafe_allow_html=True)
    
    with col4:

        fig = px.bar(df_class, x="count", y="set", color="class", color_discrete_map = {'biker': cmap["dark_green"], 'car': cmap["green"], 'pedestrian': cmap["blue_green"], 'trafficLight': cmap["yellow"], 'truck': cmap["orange"]})

        fig.update_layout(legend = dict( orientation="h", yanchor="top", y=0.02, xanchor="right", x=0.8, itemwidth=40), xaxis_showticklabels=False, xaxis_title=None, yaxis_title=None)

        st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Exploración de los datos")

    st.markdown('<div style="text-align: justify;">La exploración de los datos de entrenamiento que hemos utilizado nos permite descubrir información útil en grandes conjuntos de datos. Al comprender mejor los datos, pueden tomar decisiones más informadas y construir modelos de inteligencia artificial más precisos y efectivos. A continuación se muestra la tabla con los datos utilizados para desarrollar el modelo de red neuronal.</div>', unsafe_allow_html=True)
    
    add_vertical_space(2)

    df_data = pd.read_csv("data_info.csv")

    filtered_df = dataframe_explorer(df_data)
    
    st.dataframe(filtered_df, use_container_width=True)

# Pag 3 - Modelo

if selected == "Modelo":
 
    st_lottie(requests.get("https://assets3.lottiefiles.com/private_files/lf30_wo802rvq.json").json(), height=450, key="model")

    st.markdown("## Detección de objetos con YOLOv8")

    st.markdown('<div style="text-align: justify;">YOLOv8 es una de las versiones más recientes de la red neuronal de detección de objetos YOLO (You Only Look Once). La versión YOLOv8 se basa en una red neuronal convolucional profunda y utiliza el algoritmo de detección de objetos basado en cuadrícula para detectar y clasificar objetos en una imagen.</p><p>La detección de objetos con YOLOv8 comienza por dividir la imagen en una cuadrícula. Luego, para cada celda de la cuadrícula, se predicen los cuadros delimitadores que rodean los objetos detectados en esa celda, junto con las probabilidades de que los objetos pertenezcan a diferentes clases. Estas predicciones se realizan simultáneamente para todas las celdas de la cuadrícula, lo que permite una detección de objetos muy rápida y eficiente.</p><p>La red neuronal de YOLOv8 se entrena con una gran cantidad de imágenes etiquetadas para detectar una amplia variedad de objetos en diferentes situaciones y condiciones de iluminación. Además, YOLOv8 utiliza técnicas avanzadas de procesamiento de imágenes y aprendizaje profundo para mejorar la precisión y reducir los errores de detección.</p></p>A continuación se muestra un ejemplo de cómo trabaja la red neuronal YOLOv8 adaptada a nuestro conjunto de imágenes.<p></div>', unsafe_allow_html=True)
    
    add_vertical_space(1)

    col1, col2 = st.columns([1, 2])

    with col1:

        st.markdown("### Opciones de visualización")

        add_vertical_space(2)

        con = st.slider("Confianza", max_value=1.0, value=0.5, step=0.1)

        sup = st.slider("Superposición", max_value=1.0, value=0.3, step=0.1)

    with col2:

        add_vertical_space(1)
       
        img = f"foto_predict/con{int(con*100)}_sup{int(sup*100)}/foto.jpg"

        st.image(img, caption = "Imagen de ejemplo")

    st.markdown("""<hr style="height:2px;border:none;color:#333;background-color:#e7e7e7;" /> """, unsafe_allow_html=True)

    st.markdown("### Ejemplo")

    option = st.selectbox("Escoge una de las siguientes opciones:", ["chicago", "los_angeles", "new_york", "seattle"])

    video = f"videos_predict/{option}.mp4"

    st.video(video)

    st.markdown("## Observaciones")

    st.markdown('<div style="text-align: justify;"><p>La detección de objetos con YOLOv8 ofrece un enfoque rápido y eficiente para la detección de objetos en imágenes, lo que lo hace ideal para aplicaciones en tiempo real como la conducción autónoma, la vigilancia de seguridad y la robótica. Sin embargo, también tiene algunas limitaciones importantes que es necesario tener en cuenta.</p><p>Aunque tiene una buena precisión general en la detección de objetos, puede tener dificultades para detectar objetos muy pequeños o que ocupen solo una pequeña porción de la imagen. Su rendimiento puede disminuir en imágenes de baja resolución. Esto significa que si las imágenes que se están analizando son de baja calidad o baja resolución, la precisión de detección puede ser afectada. También tiene dificultades para clasificar objetos que tienen características visuales muy similares, que están parcialmente ocultos o que se encuentran en movimiento. Esto puede resultar en falsos positivos o negativos en la detección de objetos.</p><p>En general, YOLOv8 es una herramienta muy útil para la detección de objetos, pero es importante tener en cuenta sus limitaciones y asegurarse de que sea la opción adecuada para la tarea específica de detección de objetos que se está llevando a cabo.</p></div>', unsafe_allow_html=True)

 # Pag 4 - Resultados

if selected == "Resultados":

    st_lottie(requests.get("https://assets2.lottiefiles.com/packages/lf20_noohi61b.json").json(), height=500, key="results")

    st.markdown("## Resultados")

    st.markdown('<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</div>', unsafe_allow_html=True)

    # Histograma

    df_img = pd.read_csv("img_info.csv")

    fig = px.histogram(df_img, x=df_img.index, y="count", color="class", marginal="rug", barmode='stack', hover_data=df_img.columns, category_orders={"class":["car", "pedestrian", "trafficLight", "truck", "biker"]}, color_discrete_map = {'biker': cmap["dark_green"], 'car': cmap["green"], 'pedestrian': cmap["blue_green"], 'trafficLight': cmap["yellow"], 'truck': cmap["orange"]})

    fig.update_layout(xaxis_showticklabels=False, xaxis_title=None, yaxis_title=None, bargap=0.1)

    st.plotly_chart(fig, use_container_width=True)

    # Entrenamiento

    st.subheader("Evolución del entrenamiento")

    st.markdown('<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</div>', unsafe_allow_html=True)

    st.markdown("""<hr style="height:2px;border:none;color:#333;background-color:#e7e7e7;" /> """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    df_results = pd.read_csv("results.csv", skipinitialspace = True)

    with col1: # Class_loss 

        fig = px.line(df_results, x="epoch", y=["train/cls_loss", "val/cls_loss"], title="classification loss", color_discrete_sequence=[cmap["blue_green"], cmap["yellow"]])

        fig.data[0].name, fig.data[1].name = "train", "validation"

        fig.update_layout(yaxis_title=None, yaxis_range=[0,0.05])

        fig.update_layout(showlegend=False, xaxis_title=None)
    
        st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    with col2: # Box_loss

        fig = px.line(df_results, x="epoch", y=["train/box_loss", "val/box_loss"], title="location loss", color_discrete_sequence=[cmap["blue_green"], cmap["yellow"]])

        fig.update_layout(yaxis_title=None, yaxis_range=[0,0.05])

        fig.update_layout(legend = dict(title=None, orientation="h", y=-0.15, yanchor="top", xanchor="right", x=0.8, itemwidth=40), xaxis_title=None, yaxis_title=None)

        st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    with col3: # Object_loss

        fig = px.line(df_results, x="epoch", y=["train/obj_loss", "val/obj_loss"], title="object loss", color_discrete_sequence=[cmap["blue_green"], cmap["yellow"]])

        fig.update_layout(yaxis_title=None, yaxis_range=[0,0.05])

        fig.update_layout(showlegend=False, xaxis_title=None)

        fig.update_layout(legend = dict(title=None, orientation="h", yanchor="top", xanchor="right", x=0.8, itemwidth=40), xaxis_title=None, yaxis_title=None)

        st.plotly_chart(fig, theme="streamlit", use_container_width=True)

    # Métricas

    st.subheader("Métricas")

    st.markdown('<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</div>', unsafe_allow_html=True)

    add_vertical_space(1)

    tab1, tab2, tab3, tab4 = st.tabs(["Precisión", "Recall", "mAP50", "mAP50-95"])

    with tab1: # Precisión

        fig1 = px.line(df_results, x="epoch", y="metrics/precision")

        fig1.update_traces(line_color = cmap["blue_green"])

        fig1.update_layout(yaxis_title=None)

        st.plotly_chart(fig1, theme="streamlit", use_container_width=True)

    with tab2: # Recall

        fig2 = px.line(df_results, x="epoch", y="metrics/recall")

        fig2.update_traces(line_color = cmap["yellow"])

        fig2.update_layout(yaxis_title=None)

        st.plotly_chart(fig2, theme="streamlit", use_container_width=True)

    with tab3: # mAP50

        fig3 = px.line(df_results, x="epoch", y="metrics/mAP50")

        fig3.update_traces(line_color = cmap["orange"])

        fig3.update_layout(yaxis_title=None)

        st.plotly_chart(fig3, theme="streamlit", use_container_width=True)

    with tab4: # mAP50-95

        fig4 = px.line(df_results, x="epoch", y="metrics/mAP50-95")

        fig4.update_traces(line_color = cmap["green"])

        fig4.update_layout(yaxis_title=None)

        st.plotly_chart(fig4, theme="streamlit", use_container_width=True)

    st.subheader("Clasificación")

    st.markdown('<div style="text-align: justify;">Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</div>', unsafe_allow_html=True)

    data=[[0.77, 0, 0.01, 0.17, 0, 0.62], [0, 0.46, 0.11, 0, 0, 0.16], [0, 0.02, 0.43, 0, 0, 0.03], [0.01, 0, 0, 0.55, 0, 0.06], [0, 0, 0, 0, 0.73, 0.13], [0.22, 0.52, 0.45, 0.28, 0.27, 0]]

    fig2 = px.imshow(data, labels=dict(x="Valor real", y="Valor predicho", color="Productivity"), x=['Coche', 'Peatón', 'Ciclista', 'Camión', 'Semáforo', 'Fondo'], y=['Coche', 'Peatón', 'Ciclista', 'Camión', 'Semáforo', 'Fondo'], text_auto=True, color_continuous_scale = 'mint')
    
    fig2.update_coloraxes(showscale=False)

    fig2.update_xaxes(side="top")

    st.plotly_chart(fig2, theme="streamlit", use_container_width=True)


# streamlit run /Users/marta/Documents/GitHub/Object-detection-for-self-driving-cars/streamlit_app.py
