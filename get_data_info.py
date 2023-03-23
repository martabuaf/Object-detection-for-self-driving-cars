# Librerías

import pandas as pd
import numpy as np
from os import walk

# Directorio del dataset

dataset_dir = "/Users/marta/Documents/GitHub/Object-detection-for-self-driving-cars/"

## Cargo el dataset

# Datos de entrenamiento

train = next(walk(dataset_dir + "img_data/train/images"), (None, None, []))[2]

# Datos de validación

validation = next(walk(dataset_dir + "img_data/val/images"), (None, None, []))[2]

# Datos de prueba

test = next(walk(dataset_dir + "img_data/test/images"), (None, None, []))[2]

## Proporción del dataset

df_data = pd.read_csv(dataset_dir+"img_data/_annotations.csv")

df_data["image"] = [j.replace("_", ".") for j in [i.split(".rf.")[0] for i in df_data.filename]]

set_list =list()

for i in df_data.filename:

    if i in train:

        set_list.append("train")

    elif i in validation:

        set_list.append("validation")

    elif i in test:

        set_list.append("test")

    else:

        set_list.append("None")

df_data["set"] = set_list

semaforo = ["trafficLight-Green", "trafficLight-GreenLeft", "trafficLight-Red", "trafficLight-RedLeft", "trafficLight-Yellow", "trafficLight-YellowLeft"]	

df_data["class"] = df_data["class"].replace(semaforo, "trafficLight")

## Creo los archivos con la información sobre el dataset

# Resumen del dataset

df_data.to_csv("data_info.csv", index=False)

# Resumen de las imágenes

df_img = pd.DataFrame(df_data.sort_values("image").groupby(["image", "class"]).count().reset_index())

df_img.rename(columns={"filename": "count"}, inplace=True)

df_img.drop(df_img.columns[3:], axis=1, inplace=True)

df_img.to_csv("img_info.csv", index=False)

# Resumen de las clases

df_class = pd.DataFrame(df_data.groupby(["set", "class"]).count().reset_index())

df_class.rename(columns={"filename": "count"}, inplace=True)

df_class.drop(df_class.columns[3:], axis=1, inplace=True)

df_class.to_csv("class_info.csv", index=False)