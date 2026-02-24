import cv2
import numpy as np

img = cv2.imread('images/klown.jpg')

#ОТЗЕРКАЛИТЬ ИЗОБРАЖЕНИЕ
#img = cv2.flip(img, 1) # 0 по вертикали, 1 по горизонтали, -1 по обеим осям

#ВРАЩЕНИЕ ИЗОБРАЖЕНИЯ
def rotate(img_param, angle): # функция (переменная,угол вращения)
    height, width = img.shape[:2] # получить высоту и ширину изображения
    point = (width//2, height//2) # центр изображения
    
    rotation_matrix = cv2.getRotationMatrix2D(point, angle, 1) # матрица для вращения (центр вращения, угол вращения, масштаб)
    return cv2.warpAffine(img_param, rotation_matrix, (width, height)) # применить вращение (переменная, матрица вращения, размер изображения)
#img = rotate(img, -90) 

#СМЕЩЕНИЕ ИЗОБРАЖЕНИЯ
def transform(img_param, x, y): # функция (переменная, смещение по x, смещение по y)
    transformation_matrix = np.float32([[1, 0, x], [0, 1, y]]) # матрица для смещения (x, y, смещение по x), (x, y, смещение по y)
    height, width = img.shape[:2] # получить высоту и ширину изображения
    return cv2.warpAffine(img_param, transformation_matrix, (width, height)) # применить смещение (переменная, матрица смещения, размер изображения)
#img = transform(img, 30, 20)

#КОНТУРЫ ИЗОБРАЖЕНИЯ

new_img = np.zeros(img.shape, dtype='uint8') 

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # черно-белое изображение
img = cv2.GaussianBlur(img, (5,5), 0) #размытие
img = cv2.Canny(img, 100, 140) # границы. цвета больше 140 - белые, меньше 100 - черные, между ними - серые

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE) # найти контуры 
cv2.drawContours(new_img, con, -1, (0,255,0), 1) # нарисовать контуры (переменная для рисования, контуры, индекс контура (-1 - все), цвет, толщина)



cv2.imshow('klown', img)

cv2.waitKey(0) 