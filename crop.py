import numpy as np
import argparse
import cv2

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("ORIGINAL",image)

cropped = image[60:120,200:245]
cv2.imshow("Face",cropped)
cv2.waitKey(0)

cv2.destroyAllWindows()