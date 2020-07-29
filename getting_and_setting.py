from __future__ import print_function
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("ORIGINAL",image)

(b,g,r) = image[0,0]

print("Pixel at (0,0) - red = {},green = {},blue = {}".format(r,g,b))

image[0,0] = (0,0,255)
(b,g,r) = image[0,0]
print("Pixel at (0,0) - red = {},green = {},blue = {}".format(r,g,b))

corner = image[0:100 , 0:100]
cv2.imshow("CORNER",corner)

image[0:100,0:100] = (0,255,0)
cv2.imshow("UPDATED",image)

cv2.waitKey(0)
cv2.destroyAllWindows()