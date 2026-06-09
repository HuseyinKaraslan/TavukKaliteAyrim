# Real-Time Chicken Quality Grading System using YOLOv8 🐔🔍

[![YOLOv8](https://img.shields.io/badge/YOLO-v8-blue.svg)](https://github.com/ultralytics/ultralytics)
[![Python](https://img.shields.io/badge/Python-3.8+-yellow.svg)](https://www.python.org/)
[![Roboflow](https://img.shields.io/badge/Dataset-Roboflow-purple.svg)](https://roboflow.com/)

## 📖 About The Project

This project is a real-time computer vision system developed to automate the quality grading of chicken meat in an industrial factory environment. The system utilizes the **YOLOv8** object detection model to classify products on a conveyor belt accurately and quickly. 

The model outputs are designed to be integrated with industrial pneumatic systems to automatically separate products based on their quality grades, significantly improving packaging optimization and factory workflow.

### ✨ Key Features
* **Real-Time Detection:** High-speed inference suitable for active conveyor belts.
* **Custom Dataset:** Trained on a custom dataset of approximately 1,500 images, meticulously annotated and augmented via **Roboflow**.
* **Cloud Training:** The model architecture was trained and optimized using **Google Colab** to leverage GPU acceleration.
* **Hardware Integration Ready:** Structured to send trigger signals to pneumatic separation arms based on bounding box classifications.

## 🛠️ Technologies & Tools
* **Model:** Ultralytics YOLOv8
* **Dataset Preparation:** Roboflow
* **Training Environment:** Google Colab (GPU)
* **Inference & Image Processing:** Python, OpenCV
* **Deployment:** Local Machine / Industrial PC

