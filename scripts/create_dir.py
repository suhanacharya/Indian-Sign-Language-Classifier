import os

char = 'A'

os.mkdir('signs_data\\')

for i in range(0,26):
	os.mkdir('signs_data\\' + char + '\\')
	char = chr(ord(char) + 1)
