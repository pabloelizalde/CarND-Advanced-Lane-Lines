
###########################
#1 Calibrate the camera
###########################
import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Read image
img = mpimg.imread("camera_cal/calibration1.jpg")
plt.imshow(img)