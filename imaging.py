import numpy as np 
from PIL import ImageGrab
from cv2 import cv2
import time

def process_image(image):
    processed = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    processed = cv2.Canny(processed,threshold1 = 130, threshold2 = 250)
    return processed