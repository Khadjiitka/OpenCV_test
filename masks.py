import cv2
import numpy as np

photo = cv2.imread('images/klown.jpg')
img = np.zeros(photo.shape[:2], dtype = 'uint8') # создать черное изображение (матрица из нулей) размеров как у фото!!!

circle = cv2.circle(img.copy(), (200,150), 100, 255,-1) # круг (переменная, (центр круга), радиус, цвет, толщина обводки -1 - заливка)


img = cv2.bitwise_and(photo, photo, mask=circle) # логическое И - пересечение двух фигур
##img = cv2.bitwise_or(photo, photo, mask=circle) # логическое ИЛИ - объединение двух фигур
###img = cv2.bitwise_xor(photo, photo, mask=circle) # логическое ИСКЛЮЧАЮЩЕЕ ИЛИ - объединение двух фигур без пересечения
####img = cv2.bitwise_not(photo, photo, mask=circle) # логическое НЕ - инверсия фигуры

cv2.imshow('res', img)
cv2.waitKey(0) # ждать нажатия клавиши
