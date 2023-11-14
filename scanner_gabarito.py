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


project = rf.workspace("sust-9qaee").project("omr-scanner")

if not os.path.exists("OMR-Scanner-3"):
    dataset = project.version(3).download("yolov8")

modelo = project.version(3).model

#diretorio de imagens originais
image_dir1 = "OMR-Scanner-3/test/images"
image_dir2 = "OMR-Scanner-3/train/images"
image_dir3 = "OMR-Scanner-3/valid/images"

for filename in os.listdir(image_dir1):
    image_path = os.path.join(image_dir1, filename)
 
    #img = modelo.predict(image_path, confidence=40, overlap=30)
    #print(img)

    filenamefinal = "dataset_result/Scanner/Test/"+filename
    modelo.predict(image_path=image_path, confidence=40, overlap=30).save(filenamefinal)

for filename in os.listdir(image_dir2):
    image_path = os.path.join(image_dir2, filename)
 
    #img = modelo.predict(image_path, confidence=40, overlap=30)
    #print(img)

    filenamefinal = "dataset_result/Scanner/Train/"+filename
    modelo.predict(image_path=image_path, confidence=40, overlap=30).save(filenamefinal)

for filename in os.listdir(image_dir3):
    image_path = os.path.join(image_dir3, filename)
 
    #img = modelo.predict(image_path, confidence=40, overlap=30)
    #print(img)

    filenamefinal = "dataset_result/Scanner/Valid/"+filename
    modelo.predict(image_path=image_path, confidence=40, overlap=30).save(filenamefinal)
