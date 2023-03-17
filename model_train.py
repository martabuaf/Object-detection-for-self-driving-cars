from ultralytics import YOLO
import torch
import os

# Parámetros iniciales

yolo_path = "/Users/marta/yolov5"

data_path = "/Users/marta/Documents/GitHub/Object-detection-for-self-driving-cars"

os.environ['KMP_DUPLICATE_LIB_OK']='True'

# Entrenamiento

# Model
model = torch.hub.load("ultralytics/yolov5", "yolov5x", autoshape=True, pretrained=True)  # or yolov5n - yolov5x6, custom

# Images
img = f"{data_path}/img_class_data/1478019952686311006_jpg.rf.54e2d12dbabc46be3c78995b6eaf3fee.jpg"  # or file, Path, PIL, OpenCV, numpy, list

# Inference
results = model(img)

# Results
results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
results.show()
results.pandas().xyxy[0]