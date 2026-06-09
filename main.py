import cv2
from ultralytics import YOLO
from PIL import Image

model= YOLO('best-3.pt')

sonuc =model.predict(source='/Users/huseyincankaraslan/PycharmProjects/kaliteAyrim/IMG_5387.HEIC', save= True)

