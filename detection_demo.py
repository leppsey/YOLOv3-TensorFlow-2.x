import os
os.environ['CUDA_VISIBLE_DEVICES'] = '0'
import cv2
import numpy as np
import tensorflow as tf
from yolov3.utils import detect_image, detect_realtime, detect_video, Load_Yolo_model, detect_video_realtime_mp
from yolov3.configs import *
import shutil

def detect(image_path):
  video_path   = "test.mp4"
  yolo = Load_Yolo_model()
  detect_image(yolo, image_path, "detect.jpg", input_size=YOLO_INPUT_SIZE, show=False, rectangle_colors=(255,0,0))
  shutil.copyfile('/content/YOLOv3-TensorFlow-2.x/detect.jpg', '/content/detected.jpg')