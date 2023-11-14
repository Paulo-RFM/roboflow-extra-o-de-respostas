from roboflow import Roboflow
from ultralytics import YOLO
import cv2
import os

# Inicialize a conexão com o Roboflow
api_key = os.getenv("ROBOFLOW_API_KEY")

rf = Roboflow(api_key=api_key)

# Acesse o projeto e faça o download do conjunto de dados
project = rf.workspace("test-m7eij").project("soc_mcq")

#verificação do download do dataset
if not os.path.exists("soc_mcq-1"):
    dataset = project.version(1).download("yolov8")

modelo = project.version(1).model
image_dir1 = "soc_mcq-1/test/images"
image_dir2 = "soc_mcq-1/train/images"
image_dir3 = "soc_mcq-1/valid/images"

for filename in os.listdir(image_dir1):
    image_path = os.path.join(image_dir1, filename)
    pathFinal = "respostasFinais/provas/Test/"+filename
    modelo.predict(image_path, confidence=40, overlap=30).save(pathFinal)

for filename in os.listdir(image_dir2):
    image_path = os.path.join(image_dir2, filename)
    pathFinal = "respostasFinais/provas/Train/"+filename
    modelo.predict(image_path, confidence=40, overlap=30).save(pathFinal)

for filename in os.listdir(image_dir3):
    image_path = os.path.join(image_dir3, filename)
    pathFinal = "respostasFinais/provas/Valid/"+filename
    modelo.predict(image_path, confidence=40, overlap=30).save(pathFinal)
 

#model = YOLO("yolov8n.pt","v8")
#detecttion_output = model.predict(source="soc_mcq-1/valid/images/teste0.png", conf=0.25, save=True)

