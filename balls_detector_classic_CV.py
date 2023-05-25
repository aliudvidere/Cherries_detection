import cv2

# Загружаем изображение
image = cv2.imread(r'D:\Documents\Skoltech\DL\\final_project\\image.jpg')

# Преобразуем изображение в оттенки серого
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Применяем гауссово размытие для устранения шума
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# Применяем алгоритм Хафа для поиска кругов
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                           param1=50, param2=30, minRadius=45, maxRadius=60)

# Если круги найдены, то отрисовываем их на изображении
if circles is not None:
    circles = circles[0]
    print(circles)
    for (x, y, r) in circles:
        cv2.rectangle(image, (int(x - r), int(y - r)), (int(x + r), int(y + r)), (0, 0, 255), 2)

# Сохраняем результат
cv2.imwrite(r'D:\Documents\Skoltech\DL\\final_project\\result.jpg', image)