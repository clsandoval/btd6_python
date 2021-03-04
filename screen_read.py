import numpy as np 
from PIL import ImageGrab
from cv2 import cv2
from test_functions import test
from imaging import process_image
import sys
import time
import pyautogui
import win32api
last_time = time.time()
state_left = win32api.GetKeyState(0x01)  # Left button down = 0 or 1. Button up = -127 or -128
state_right = win32api.GetKeyState(0x02)  # Right button down = 0 or 1. Button up = -127 or -128
first_img = np.array(ImageGrab.grab(bbox = (0,33,640,430)))

#define the dataset arrays
imgdata = np.array([first_img])
mouseclicks = np.array([[0,0]])

#testing mouse clicks
#test()
i = 0
while True:
    x,y = (0,0)
    a = win32api.GetKeyState(0x01)
    if a < 0:
        x,y = win32api.GetCursorPos()
        print(x,y)
        print(x,y,file=sys.stderr)
    else:
        print(x,y)
        #print(x,y,file=sys.stderr)
    mouseclicks = np.append(mouseclicks, [[x,y]], axis= 0)
    pscreen_pil = np.array(ImageGrab.grab(bbox = (0,33,640,430)))
    #imgdata = np.append(imgdata,[pscreen_pil],axis = 0)

    #print(imgdata.shape)
    #print(mouseclicks.shape)
    #print(time.time() - last_time)
    #last_time = time.time()

    #cv2.imshow('window', cv2.cvtColor(pscreen_pil, cv2.COLOR_BGR2RGB))
    cv2.imshow('window', process_image(pscreen_pil))
    cv2.waitKey()
    cv2.imwrite("map_{}.jpg".format(i), process_image(pscreen_pil))
    i+=1
    if (cv2.waitKey(1000) & 0xFF == ord('q')):
        cv2.destroyAllWindows()
        break