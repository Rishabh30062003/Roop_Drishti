import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO
import numpy as np
from ultralytics import YOLO

model = YOLO("best.onnx", task="detect")

input_width,input_height = 640,640
def detection(image,conf_threshold = 0.5):
    
    image = cv2.resize(image, (input_width, input_height))
    
    results = list(model.predict(image, imgsz=640, conf=conf_threshold, iou=0.5,stream=True,device = "cpu"))
    for result in results:
        n = len(result.boxes)
    new_image = np.array(results[0].plot())
    return cv2.resize(new_image, (500, 500)),n

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    img,n = detection(frame,conf_threshold=0.5)
    plt.title(f'No of faces = {n}')
    plt.imshow(img)  
    plt.pause(1e-10)  
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
plt.close()