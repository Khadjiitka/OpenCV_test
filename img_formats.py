import cv2

img = cv2.imread('images/klown.jpg')
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # черно-белое изображение
##img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # цветовое пространство HSV 
img = cv2.cvtColor(img, cv2.COLOR_BGR2LAB) # цветовое пространство LAB (L - яркость, A - красно-зеленый, B - желто-синий)
img = cv2.cvtColor(img, cv2.COLOR_LAB2BGR) # обратно в цветное изображение
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # цветовое пространство RGB (для отображения в matplotlib)

#РАЗДЕЛЕНИЕ СЛОЕВ
r, g, b = cv2.split(img) # разделить на каналы 

img = cv2.merge((b, g, r)) # объединить каналы обратно в изображение



cv2.imshow('result', img)
cv2.waitKey(0) 