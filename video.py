import cv2
import numpy as np

cap = cv2.VideoCapture('images/vidosek.MOV') 
while True:
    success, img = cap.read()
    
    img = cv2.GaussianBlur(img, (5,5), 0) #размытие
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # черно-белое изображение
    img = cv2.Canny(img, 30, 30) # границы
    kernel = np.ones((5,5), np.uint8) # матрица 5х5 где все элементы 1
    img = cv2.dilate(img, kernel) # расширить границы
    img = cv2.erode(img, kernel) # сузить границы

    cv2.imshow('video', img)

    if cv2.waitKey(1) & 0xFF == ord ('q'): 
        break
    # для корректного отображения & отслеживать клавишу q и ее код для выхода




##cap = cv2.VideoCapture(0) # 0 - видео с камеры, 1 - видео с внешнего устройства, 'путь' - видео с файла
##cap.set(3, 640) # ширина видео
##cap.set(4, 480) # высота видео



#cap = cv2.VideoCapture('images/vidosek.MOV')
#while True:
#   success, img = cap.read()
#   cv2.imshow('video', img)
#
#    if cv2.waitKey(1) & 0xFF == ord ('q'): 
#        break
#    # для корректного отображения & отслеживать клавишу q и ее код для выхода
