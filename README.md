# 👤 Roop_Drishti: Face Recognition System in Crowded Environments

**Real-Time Face Detection and Gender Classification using YOLOv12 and CNN**

![project banner](https://img.shields.io/badge/Deep%20Learning-YOLOv12-blue?style=for-the-badge) ![status](https://img.shields.io/badge/Status-Active-yellow?style=for-the-badge)

---

## 🧠 Project Overview

**Roop Drishti** is a deep learning-powered face recognition system designed for real-time **face detection** in **crowded environments** and **gender classification** using computer vision techniques.

- Utilizes **YOLOv12** for fast and accurate face detection.
- Employs a **Convolutional Neural Network (CNN)** for gender classification.
- Built to work in **real-time** with webcam feeds or video streams.
- Aimed at improving crowd analysis, surveillance, and demographic insights.

---

## 🚀 Key Features

- 🎯 **High Accuracy** face detection using state-of-the-art YOLOv12 model.
- 👥 Detects **multiple faces simultaneously** in dense crowd scenes.
- ⚧️ Classifies gender in real-time using a fine-tuned CNN model.
- 🧠 Smart preprocessing with OpenCV for enhanced performance.
- 📷 Live camera feed interface for practical deployment.

## **🔧 Installation & Setup**
1. Clone the repository
git clone https://github.com/Rishabh30062003/Roop_Drishti.git
cd Roop_Drishti

2. Create a virtual environment (optional but recommended)
python -m venv env
source env/bin/activate      # Linux/Mac
env\Scripts\activate         # Windows

3. Install dependencies
pip install -r requirements.txt

4. Download and place model weights
Place YOLOv12 weights inside models/yolo_v12_weights/
Place trained CNN model inside models/gender_classification/

5. Run the app
python webcam.py


## **🧪 Technologies Used**
Tool/Framework	Purpose
Python	Programming Language
OpenCV	Image Processing
YOLOv12	Face Detection
CNN (TensorFlow/Keras)	Gender Classification
Flask	Web Framework for UI
HTML/CSS	Frontend
NumPy	Numerical Operations
Matplotlib/Seaborn	Data Visualization (Notebook)

## **📊 Model Performance**
🟢 Face Detection (YOLOv12)
Precision: 92%
Recall: 88%
mAP@50: 95%

## **🟣 Gender Classification (CNN)**
Accuracy: ~93% (after fine-tuning)
Dataset: Combination of labeled public datasets for Male/Female
Image size: 96x96 RGB

## **🖼️ Output Snapshots**
![image](https://github.com/user-attachments/assets/c6eed5aa-7d33-44db-8ed1-c19446193ba2)
![Screenshot 2025-06-07 184447](https://github.com/user-attachments/assets/56b9ff74-3158-4d55-bcbd-33ab39039ca1)

## **📌 Applications**
👮‍♂️ Security Surveillance in public places
🎤 Event Monitoring for demographic stats
🏬 Retail Analytics in malls/stores
🧪 Academic Research in computer vision

## **⚠️ Limitations**
Struggles in extremely low-light or highly occluded conditions.
Gender classification limited to binary labels.
Requires GPU for real-time performance in large-scale environments.

## **💡 Future Enhancements**
🧓 Add Age Estimation model
🌐 Deploy as a complete cloud-based API
🕶️ Include face recognition (identity verification)
📈 Real-time dashboard for analytics

## **🤝 Acknowledgements**
YOLOv12 Official GitHub
OpenCV
Keras & TensorFlow
Roboflow Dataset Platform

## **🧑‍💻 Author**
Rishabh Kumar
B.Tech CSE (AI) Final Year
📧 Email: rishabhkumarjajauli@gmail.com
🐙 GitHub: @Rishabh30062003
🔗 LinkedIn: linkedin.com/in/Rishabh Kumar
