<h1 style="text-align:center;">Detección de objetos para conducción autónoma</h1>

<p align="center"><img src="https://user-images.githubusercontent.com/122131317/227728740-7b38151f-f415-4fc9-9cd8-efcdff5b5606.jpg" width="600"></p>

<h3>Resumen:</h3>
<p>El objetivo de este proyecto es detectar objetos en tiempo real pertenecientes a coches, peatones, ciclistas, camiones y semáforos, para la conducción autónoma. Para ello analizaremos imágenes de la vía pública, con el objetivo de que nuestro sistema localice y clasifique los diferentes objetos contenidos en las imágenes sin necesidad de supervisión humana. El conjunto de datos que hemos utilizado lo encontramos en <a href="https://www.kaggle.com/datasets/sshikamaru/udacity-self-driving-car-dataset" target = "_blank"> Kaggle</a>.</p>
<p>El conjunto de datos comprende más de 22 mil imágenes de conducción e información sobre los elementos ya etiquetados en las imágenes. Utilizando estos datos, entrenaremos un modelo de red neuronal preentrenada YOLOv8, que detectará e identificará los objetos comprendidos en una de estas 5 clases: coches, peatones, ciclistas, camiones y semáforos. Para ello divideremos los datos en datos de entrenamiento y datos de prueba.</p>

<h3>Paso 1: Carga y procesamiento de los datos</h3> 
<p>Procesaremos las imágenes y las convertiremos al formato necesario para llevar a cabo el entrenamiento de YOLOv8.</p>
<h3>Paso 2: División del conjunto de datos</h3> 
<p>Dividiremos las imágenes en 3 subconjuntos de datos: entrenamiento (train), validación (val) y pruebas (test).</p>
<h3>Paso 3: Entrenamiento</h3> 
<p>Llevaremos a cabo el entrenamiento de la red para adaptar su funcionamiento a nuestro conjunto de datos. Establecimos una duración del entrenamiento de 20 epochs. Una vez entrenado guardaremos los mejores pesos alcanzados y evaluremos los resultados de precisión y pérdida para ajustar el entrenamiento.
<h3>Paso 4: Prueba</h3>
<p>Probaremos el modelo sobre el conjunto de datos de prueba y obtendremos la matriz de confusión resultante.</p>
<h3>Paso 5: Integración</h3> 
<p>Una vez que tenemos el modelo listo, lo integraremos con Streamlit Share y lo probaremos sobre nuevos datos. Encontrarás nuestro proyecto en el siguiente <a href = "https://martabuaf-object-detection-for-self-drivin-streamlit-app-ccbm59.streamlit.app">enlace</a>.</p>
<p>Aquí puedes ver un ejemplo de los resultados!⬇️</p>

https://user-images.githubusercontent.com/122131317/227729596-ed057f75-dded-495a-aa62-feed3811ce24.mp4

<h2 style="text-align:center;">Esperamos que te guste!! 😄</h2>

## Autores: 
<p>Marta Búa Fernández ➡️ Ir al perfil de<a href="https://www.linkedin.com/in/martabuaf" target = "_blank"> LinkedIn </a></p> 
<p>Laura Arufe Jorge ➡️ Ir al perfil de<a href="https://www.linkedin.com/in/laura-arufe-aab862247" target = "_blank"> LinkedIn </a></p>

