import cv2
import numpy as np
import os

char = 'A'
for i in range(0,26):
	if char == 'I':
		char = chr(ord(char) + 1)
		i = i+1
		continue
	vidcap = cv2.VideoCapture('video2\\' + char + '.mp4')
	success,image = vidcap.read()
	count = 0
	success = True
	while success:
		cv2.imwrite('signs_data\\' + char + "\\" + char + "frontframe%d.jpg" % count, image)     # save frame as JPEG file
		success,image = vidcap.read()
		print(char + ' Read a new frame' + str(count) + ': ', success)
		count += 1
	count = 0
	char = chr(ord(char) + 1)
