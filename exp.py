import numpy as np
import cv2

image = cv2.imread("messi.jpg")

(h,w) = image.shape[:2]

height = h*2
width = w*2
k1 = 0
k2 = 0

canvas = np.zeros((height,width,3),dtype='uint8')

for i in range(h):
    for j in range(w):
        k1 = i*2
        k2 = j*2
        canvas[k1:k1+2,k2:k2+2] = image[i,j]

cv2.imshow("ORIGINAL",image)
cv2.imshow("SCALED",canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
