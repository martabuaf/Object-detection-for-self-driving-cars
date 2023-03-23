from ultralytics import YOLO
import torch
import os

# Parámetros iniciales

yolo_path = "/Users/marta/yolov5"

data_path = "/Users/marta/Documents/GitHub/Object-detection-for-self-driving-cars"

os.environ['KMP_DUPLICATE_LIB_OK']='True'

# Entrenamiento

# Model
#model = torch.hub.load("ultralytics/yolov5", "yolov5n", classes=5)  # or yolov5nu

model = torch.hub.load('ultralytics/yolov5', 'custom', path='best.pt',force_reload=True, source='local', pretrained=False)

#model.load_state_dict(torch.load(data_path+'/best.pt')['model'].state_dict())

# Images
img = f"{data_path}/img_data/1478019952686311006_jpg.rf.54e2d12dbabc46be3c78995b6eaf3fee.jpg"  # or file, Path, PIL, OpenCV, numpy, list

# Inference
results = model(img)

# Results
results.print()  # or .show(), .save(), .crop(), .pandas(), etc.
results.show()
results.pandas().xyxy[0]