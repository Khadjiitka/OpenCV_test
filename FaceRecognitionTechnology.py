import cv2

img = cv2.imread('images/international.jpg')

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # черно-белое изображение

#faces = cv2.CascadeClassifier('faces.xml') # загрузить классификатор для распознавания лиц
faces = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

results = faces.detectMultiScale(img_gray, scaleFactor=2, minNeighbors=4) # найти лица (переменная, размер лиц, минимальное количество соседей для подтверждения лица)

for (x, y, w, h) in results: # для каждого найденного лица (координаты x и y, ширина и высота)
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2) # нарисовать прямоугольник вокруг лица (переменная, начальная точка, конечная точка, цвет, толщина)

cv2.imshow('res', img)
cv2.waitKey(0) # ждать нажатия клавиши