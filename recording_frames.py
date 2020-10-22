import cv2 as cv
import numpy
from os import system as s
from os import path as p
from threading import Timer
webcamera=cv.VideoCapture(0)
fourcc=cv.VideoWriter_fourcc(*'XVID')
out=cv.VideoWriter('output.avi',fourcc,20.0,(640,480))
s('mkdir imagescaptured')
x=0
c=-20

seconds=int(input('interval for image capture ? : '))
print("press q to end all processes")
while True:
	ret,frame=webcamera.read()
	out.write(frame)
	if x==c+20*seconds:
		c=x
		cv.imwrite(f'./imagescaptured/{x/20}.png',frame)
	cv.imshow('frame',frame)
	x+=1
	if cv.waitKey(1) & 0xFF == ord('q'):
		break

webcamera.release()
out.release()
cv.destroyAllWindows()