from roboflow import Roboflow
from ultralytics import YOLO
import cv2
import os

# Inicialize a conexão com o Roboflow
api_key = os.getenv("ROBOFLOW_API_KEY")
print(api_key)
rf = Roboflow(api_key=api_key)

# Acesse o projeto e faça o download do conjunto de dados
project = rf.workspace("test-m7eij").project("soc_mcq")

#verificação do download do dataset
if not os.path.exists("soc_mcq-1"):
    dataset = project.version(1).download("yolov8")

modelo = project.version(1).model
image_dir = "soc_mcq-1/valid/images"
for filename in os.listdir(image_dir):
    image_path = os.path.join(image_dir, filename)
    print(image_path)   
    img = modelo.predict(image_path, confidence=40, overlap=30).json()
    modelo.predict(image_path, confidence=40, overlap=30).save()
    val = img['predictions'][0]
    class_ = val['class']
    print(class_)

#model = YOLO("yolov8n.pt","v8")
#detecttion_output = model.predict(source="soc_mcq-1/valid/images/teste0.png", conf=0.25, save=True)

