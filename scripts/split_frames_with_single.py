
import cv2
import numpy as np
import os

vidcap = cv2.VideoCapture('compression.mp4')

success,image = vidcap.read()
count = 0
success = True
while success:
	for i in range(0,30):
		success,image = vidcap.read()
	if not success: break	
	cv2.imwrite('Data\\' + "frame%d.jpg" % count, image)     # save frame as JPEG file
	success,image = vidcap.read()
	print(' Read a new frame' + str(count) + ': ', success)
	count += 1
	if not success: break

