from os import remove
import os


#ELIMINAMOS LAS IMAGENES SIN ETIQUETA
labels = os.listdir("C:\\Users\\laruj\\Desktop\\PROYECTO 4\\imagenes\\labels_2")
imagenes= os.listdir("C:\\Users\\laruj\\Desktop\\PROYECTO 4\\imagenes\\images")    
for i in labels:
    imagenes.remove(f"{i[:-4]}.jpg")
for i in imagenes:
    remove(f"C:\\Users\\laruj\\Desktop\\PROYECTO 4\\imagenes\\images\\{i}")