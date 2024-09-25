import cv2
import numpy as np

# Load the image
image = cv2.imread(r'D:\HUST\20241\IT4432E - Biometrics\capstone project\Hoc Tren Lop\image.jpg')

# Convert BGR to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_bound = np.array([13, 50, 50])
upper_bound = np.array([43, 255, 255])

mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

result = cv2.bitwise_and(image, image, mask=mask)
result[mask > 0] = [255, 255, 255] 
result[mask == 0] = [0, 0, 0]

cv2.imshow('Result Image', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
