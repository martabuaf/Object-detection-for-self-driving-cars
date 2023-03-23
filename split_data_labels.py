# Librerías

import pandas as pd
import os
from sklearn.model_selection import train_test_split
import shutil

# Directorio del dataset

dataset_dir = "/Users/marta/Documents/GitHub/Object-detection-for-self-driving-cars/img_data/"

# Leo las imágenes

images = [dataset_dir + x for x in os.listdir(dataset_dir)]

images.sort()

# Divido el dataset

train, test = train_test_split(images, test_size = 0.3, random_state = 123)

train, val = train_test_split(train, test_size = 0.2, random_state = 123)

# Muevo las imágenes a las carpetas

def move_files_to_folder(list_of_files, destination_folder):

    for file in list_of_files:

        archivo = file.split("/")[-1]

        try:

            shutil.copy(file, f"{destination_folder}/{archivo}")

        except:
             
             print(file)

move_files_to_folder(train, dataset_dir + "train/images")

move_files_to_folder(val, dataset_dir + "val/images")

move_files_to_folder(test, dataset_dir + "test/images")

# Creo los archivos con las etiquetas

df = pd.read_csv(dataset_dir+"_annotations.csv")

df['class'].replace(['trafficLight-Red', 'trafficLight-Green', 'trafficLight-RedLeft', 'trafficLight-GreenLeft'], 'trafficLight', inplace=True) # Reducimos el número de clases de semaforos

dict = {"car":0, "pedestrian":1, "biker":2, "truck":3, "trafficLight":4}

def create_labels(list_of_files, destination_folder):

    for file in list_of_files:

        archivo = file.split("/")[-1]

        df_file = df[df["filename"] == archivo]

        f = open(f"{destination_folder}/{archivo[:-4]}.txt", "w") 

        detecciones = df_file.shape[0]

        for i in range(detecciones):

            d = df_file.iloc[i]

            X = (d["xmin"] + (d["xmax"] - d["xmin"]) / 2) / 512

            Y = (d["ymin"] + (d["ymax"] - d["ymin"]) / 2) / 512

            width = (d["xmax"] - d["xmin"]) / 512

            height = (d["ymax"] - d["ymin"]) / 512

            clase = dict.get(d["class"])

            f.write(f"\n {clase} {X} {Y} {width} {height}")

        f.close()

create_labels(train, dataset_dir + "train/labels")

create_labels(val, dataset_dir + "val/labels")

create_labels(test, dataset_dir + "test/labels")

# Eliminar el archivo _annotations.csv de las carpetas de train,val,test