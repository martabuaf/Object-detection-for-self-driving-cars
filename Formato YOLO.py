import pandas as pd
from os import remove
import os

# Parámetros iniciales

dataset_dir = "/Users/marta/Documents/GitHub/Object-detection-for-self-driving-cars/"

#Convertimos las distintas etiquetas de semaforos en una unica

df = pd.read_csv(dataset_dir+"img_data/_annotations.csv")

df['class'].replace(['trafficLight-Red', 'trafficLight-Green', 'trafficLight-RedLeft', 'trafficLight-GreenLeft'], 'trafficLight', inplace=True)

dict={"car":0, "pedestrian":1, "biker":2, "truck":3, "trafficLight":4}

#FORMATO YOLO 

for i in (df["filename"].unique()):

    f = df[df["filename"] == i]

    file = open(f"C:\\Users\\laruj\\Desktop\\PROYECTO 4\\imagenes\\labels\\{i[:-4]}.txt", "w")

    detecciones=f.shape[0]

    for i in range(detecciones):

        d = f.iloc[i]

        X = (d["xmin"] + (d["xmax"] - d["xmin"]) / 2) / 512

        Y = (d["ymin"] + (d["ymax"] - d["ymin"]) / 2) / 512

        width = (d["xmax"] - d["xmin"]) / 512

        height = (d["ymax"] - d["ymin"]) / 512

        clase = dict.get(d["class"])

        file.write(f"\n {clase} {X} {Y} {width} {height}")

    file.close()

