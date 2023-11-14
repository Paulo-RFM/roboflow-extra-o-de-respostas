from cProfile import label
from numpy import imag
from sympy import false
from ultralytics import YOLO
import cv2
import os
from roboflow import Roboflow
import matplotlib.pyplot as plt

# Inicialize a conexão com o Roboflow
api_key = os.getenv("ROBOFLOW_API_KEY")
rf = Roboflow(api_key=api_key)

project = rf.workspace("srinakharinwirot-university-ayja3").project("omr-detect")

#verificação do dataset
if not os.path.exists("OMR-Detect-1"):
    dataset = project.version(1).download("yolov8")
modelo = project.version(1).model

project_scan = rf.workspace("sust-9qaee").project("omr-scanner")

#verificação do download de Scanner de questoes
if not os.path.exists("OMR-Scanner-3"):
    dataset = project_scan.version(3).download("yolov8")
modelo_scan = project_scan.version(3).model


image_dir1 = "OMR-Detect-1/test/images"
image_dir2 = "OMR-Detect-1/train/images"
image_dir3 = "OMR-Detect-1/valid/images"

for filename in os.listdir(image_dir1):
    image_path = os.path.join(image_dir1, filename)
 
    filenamefinal = "dataset_result/ORM1/predictTest/"+filename
    modelo.predict(image_path=image_path, confidence=40, overlap=30,labels=false).save(filenamefinal)

    pathFinal = 'respostasFinais/OMR1/Test/'+filename
    modelo_scan.predict(filenamefinal,confidence=40, overlap=30).save(pathFinal)

for filename in os.listdir(image_dir2):
    image_path = os.path.join(image_dir2, filename)
 
    #img = modelo.predict(image_path, confidence=40, overlap=30)
    #print(img)
    filenamefinal = "dataset_result/ORM2/predictTrain/"+filename
    modelo.predict(image_path=image_path, confidence=40, overlap=30,labels=false).save(filenamefinal)

    project2 = rf.workspace("sust-9qaee").project("omr-scanner")
   
    pathFinal = 'respostasFinais/OMR1/Train/'+filename
    modelo_scan.predict(filenamefinal,confidence=40, overlap=30).save(pathFinal)

for filename in os.listdir(image_dir3):
    image_path = os.path.join(image_dir3, filename)
 
    filenamefinal = "dataset_result/ORM2/predictValid/"+filename
    modelo.predict(image_path=image_path, confidence=40, overlap=30,labels=false).save(filenamefinal)

    project2 = rf.workspace("sust-9qaee").project("omr-scanner")
   
    pathFinal = 'respostasFinais/OMR1/Valid/'+filename
    modelo_scan.predict(filenamefinal,confidence=40, overlap=30).save(pathFinal)


 