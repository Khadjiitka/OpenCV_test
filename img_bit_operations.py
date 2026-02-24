import cv2
import numpy as np

img = np.zeros((300, 300, 3), np.uint8) # создать черное изображение (матрица из нулей) (высота, ширина, кол-во каналов FRGB => в дальнейшем можно окрасить)

circle = cv2.circle(img.copy(), (0,0), 100, 255,-1) # круг (переменная, (центр круга), радиус, цвет, толщина обводки -1 - заливка)
square = cv2.rectangle(img.copy(), (20,20), (250,250), 255, -1) #  прямоугольник (переменная, (начальная точка), (конечная), цвет, толщина обводки thickness=cv2.FILLED - заливка)
##cv2.imshow('square', square)

#img = cv2.bitwise_and(circle, square) # логическое И - пересечение двух фигур
##img = cv2.bitwise_or(circle, square) # логическое ИЛИ - объединение двух фигур
img = cv2.bitwise_xor(circle, square) # логическое ИСКЛЮЧАЮЩЕЕ ИЛИ - объединение двух фигур без пересечения
###img = cv2.bitwise_not(circle) # логическое НЕ - инверсия фигуры

cv2.imshow('res', img)
cv2.waitKey(0) # ждать нажатия клавиши
