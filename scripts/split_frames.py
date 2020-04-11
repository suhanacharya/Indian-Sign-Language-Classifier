import cv2
import numpy as np
import os

vidcap = cv2.VideoCapture('video2\\Z.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
  cv2.imwrite("Z\\Zframe%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
